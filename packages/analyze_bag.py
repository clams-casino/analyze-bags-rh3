import rosbag
import numpy as np
import os

# Assume bags always mounted to this directory in the docker container
bag_dir = '/bags/'

# Assume that we pass the bag name into the docker image using an environment variable
bag_name = os.environ['BAG_NAME']
bag_path = bag_dir + bag_name


class TopicStats():
    def __init__(self, topic):
        self.topic = topic
        self.prev_msg_time = None
        self.periods = []
        self.num_msgs = 0

    def addMsg(self, msg_time):
        self.num_msgs = self.num_msgs + 1

        if self.prev_msg_time:
            self.periods.append(msg_time - self.prev_msg_time)
        
        self.prev_msg_time = msg_time

    def printStats(self):
        stats = self.topic + '\n' + \
                'num messages:{} \nperiod:\n'.format(self.num_msgs) + \
                '  min:{:.2f}\n'.format(np.amin(self.periods)) + \
                '  max:{:.2f}\n'.format(np.amax(self.periods)) + \
                '  average:{:.2f}\n'.format(np.mean(self.periods)) + \
                '  median:{:.2f}\n'.format(np.median(self.periods))
        print(stats)


topics = {}
print('Analyzing {}'.format(bag_path))
bag = rosbag.Bag(bag_path)
for topic, msg, t in bag.read_messages():
    if topic not in topics:
        topics[topic] = TopicStats(topic)
    topics[topic].addMsg(msg.header.stamp.to_sec())
bag.close()

for topic, topic_stats in topics.items():
    topic_stats.printStats()
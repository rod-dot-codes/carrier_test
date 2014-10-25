#!/usr/bin/python
import etcd
import time
import random
import os

def whose_the_leader(node_id):
	""" Check who the leader of the carrier_test application and if no-one is leader, make me the leader.
	"""
	while True:
		client = etcd.Client(host='172.17.42.1',port=4001)
		#Tell my peers that I exist
		client.write('/carrier_test/%s' % node_id, 1,ttl=61)
		#Is there a leader available
		result = client.read('/carrier_test/leader')
		if result.value == None:
			#Try to become leader
			result.value = node_id
			result.ttl = 10 #TTL of 10 seconds till it expires
			try:
				print "Trying to become the leader"
				updated = Client.update(result)
				print "I am the leader"
			except:
				print "Damn, someone became leader before me"
		sleep_duration = int(random.randrange(0,60))
		print "Sleeping for %s seconds" % (sleep_duration)

if __name__ == "__main__":
	node_id = os.environ.get('node_id')
	print "Node ID is %s" % node_id
	whose_the_leader(node_id)
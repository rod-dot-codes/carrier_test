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
		try:
			result = client.read('/carrier_test/leader')
			if result.value == str(node_id):
				print "I AM THE LEADER"
		except:
			result = client.write('/carrier_test/leader', str(node_id),ttl=20)
			print result

		sleep_duration = int(random.randrange(0,60))
		print "Sleeping for %s seconds" % (sleep_duration)
		time.sleep(sleep_duration)

if __name__ == "__main__":
	node_id = os.environ.get('node_id')
	print "Node ID is %s" % node_id
	whose_the_leader(node_id)
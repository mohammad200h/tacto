#!/usr/bin/env python

import pybullet as p

from mamad_util import JointInfoURDF




finger = "full"



if __name__ == '__main__':
	p.connect(p.GUI)
	robot = p.loadURDF("allegro_hand_description_left_digit.urdf")

	jointInfo = JointInfoURDF()
	jointInfo.get_infoForAll_joints(robot)
	jointInfo.show_infoForAll_joints()

	link_index_dic = {
		"link_15.0_tip":None,
		"link_3.0_tip":None,
		"link_7.0_tip":None,
		"link_11.0_tip":None
	}
	
	for link_name in link_index_dic.keys():
		link_name_encoded = link_name.encode(encoding='UTF-8',errors='strict')
		Info = jointInfo.searchBy(key="linkName",value = link_name_encoded)[0]
		# print("Info:: ",Info)
		jointIndex = Info["jointIndex"]
		# print(link_name+"::jointIndex:: ",jointIndex)
		
		link_index_dic[link_name]= jointIndex

	print(link_index_dic)
	while(1):
		
		# shadowHand = robot[0]
		p.setRealTimeSimulation(1)
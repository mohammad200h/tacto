#!/usr/bin/env python

import pybullet as p

from mamad_util import JointInfoURDF


from modelGenerator import DomainRandomization

finger = "full"

dr = DomainRandomization(load_ws=True,load_ws_pcd = False)
# dr.visual_randomization()
dr.save_setting()
dr.generate_model_sdf(control_mode=finger)

if __name__ == '__main__':
	p.connect(p.GUI)
	robot = p.loadURDF("./model_"+finger+".urdf")

	jointInfo = JointInfoURDF()
	jointInfo.get_infoForAll_joints(robot)
	jointInfo.show_infoForAll_joints()

	link_index_dic = {
		"distal_FF":None,
		"distal_MF":None,
		"distal_RF":None,
		"thdistal":None
	}
	
	for link_name in ["distal_FF","distal_MF","distal_RF","thdistal"]:
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
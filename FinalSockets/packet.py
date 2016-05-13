#!/usr/bin/python
import os

class Packet: 
	def __init__(self, req, CandidateID, action):
		self.req = req
		self.CandidateID = str(CandidateID)
		self.action = action
	
	def stream(self):
		return self.req+ ' ' +self.CandidateID+ ' ' +self.action

	def printing(self):
		print self.req,', ',self.CandidateID,', ',self.action

	def rxPacket(self, Packet):
		self.req = Packet[1:4]
		self.CandidateID = Packet[5]
		self.action = Packet [6:(len(Packet)-1)]

	def toBin(self):

		toSend = self.stream()
		return ''.join([bin(ord(ch))[2:].zfill(8) for ch in toSend])


	




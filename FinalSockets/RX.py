


class Packet: 
	def __init__(self, Packet):
		self.req = Packet[0:3]
		self.CandidateID = Packet[4]
		self.action = Packet [6:(len(Packet))]
	
	def getattr(self):
		return self.req+ ' ' +self.CandidateID+ ' ' +self.action

	def printing(self):
		print self.req,', ',self.CandidateID,', ',self.action

	
	def desicion(self, candidates):

		if self.action == "vote":
			candidates[int(self.CandidateID)]+=1

		
		return Packet("res "+self.CandidateID+" "+str(candidates[int(self.CandidateID)]))

        def toBin(self):
                toSend = self.getattr()
                return "".join([bin(ord(ch))[2:].zfill(8) for ch in toSend])

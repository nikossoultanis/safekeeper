class CentralOffice:
	@staticmethod
	def notifyIncorrectPin(time, pin, sector):
		print(f'time: {time}, pin: {pin}, sector: {sector}')
		# send to some random server
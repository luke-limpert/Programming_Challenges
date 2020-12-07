def wash_hands(N, nM):
	return str(int((N*30*nM*21-((N*30*nM*21)%60))/60)) + " minutes and " + str(int((N*30*nM*21)%60)) + " seconds"
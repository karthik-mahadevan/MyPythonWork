user_list = ["user 1", "user 2"]
service_list = ["web marketing", "SEO", "data analytics"]
user_score_factors = {"user 1" : {"web marketing" : 2, "SEO" : 0.5}, "user 2" : {"web marketing" : 3, "data analytics" : 4}}


for user in user_list:
	for service in service_list:
		try : 
			print user, service, user_score_factors[user][service] 
		except : 
			user_score_factors[user][service] = 1
			print user_score_factors[user][service] 
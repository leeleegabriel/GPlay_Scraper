with open("server.txt", "r") as file:
	server_list = file.readlines()

with open("lee.txt", "r") as file:
	lee_list = file.readlines()

rm_list = []
for line in lee_list:
	if line in server_list:
		rm_list.append(line)

rm_file = open("rm.txt", "w")
for line in rm_list:
  rm_file.write("%s" % line)

print "server apks: ", len(server_list)
print "lee apks: ", len(lee_list)
print "rm apks: ", len(rm_list)
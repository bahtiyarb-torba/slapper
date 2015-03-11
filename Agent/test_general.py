import general

systemInfo = general.SystemInfo()
print "Your OS type is " + systemInfo.get_os_type()

mem_total, mem_used = systemInfo.get_memory_usage()
print "Your Memory usage is " + str(mem_used) + " of a " + str(mem_total)

print "Size if a directory size of /root is " + str(systemInfo.get_folder_size('/root'))


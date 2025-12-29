a=[100,200] #list creation

print(type(a))

a.append(500)

clouds = list({}) #list creation using list constructor

print(type(clouds))

clouds.append("aws")
clouds.append("azure")
clouds.append("gcp")
clouds.append("ibm")
clouds.append("alibaba")
clouds.append("utho")
print("Length of list of clouds is: ", len(clouds))
print("World leader for cloud service provider is", clouds[0])
print("Indian cloud service provider is: ", clouds[-1])

print(dir(clouds))
clouds.extend(["digitalocean","linode"])
print("Updated list of clouds: ", clouds)

#rang(5) => 0,1,2,3,4
for cloud in clouds:
    if cloud == 'aws':
        print(cloud, "is the market leader for cloud services")
        break
#Iterating through the list
for cloud in clouds:
    print(cloud)

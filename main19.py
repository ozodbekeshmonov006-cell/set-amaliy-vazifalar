set1={"Artel","Alif","Yandex", "Google", "Meta"} 
set2={"Google", "Apple", "Amazon", "Meta"}
set3={"Alibaba", "Uzum", "Meta", "Google", "Amazon"}
umumiy = set1.intersection(set2).intersection(set3)
umumiybulmagan = set1.difference(set2).difference(set3)
print("umumiy elemintlar"," ,",umumiy)
print("faqat birinchi set"," ,",umumiybulmagan)
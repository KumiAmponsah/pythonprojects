declare = ["I am excelling in academics", "I am excelling in sports",
           "I am excelling in business, my companies, institutions", "I am a Christian Billionaire",
           "I am healthy", "I have a beautiful and godly wife", "I have a successful and blessed marriage",
           "I have a wealthy and healthy family", "I am a blessing to Africa, Ghana, and the world",
           "I am excelling in my ministrations", "The grace , favour of the Lord is upon me",
           "I have grace and favour before God and men", "I have wonderful and godly kids",
           "My wife's pregnancy and labour is healthy and successful one"]


yep = ("Y", "y")
y = 0
for x in declare:
    y += 1
    print(declare[y-1])
    yes = input("Y/N \n")
    if yes not in yep:
        print("Do it")
        print(declare[y - 1])
        print("Rerun")
        break

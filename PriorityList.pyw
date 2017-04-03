'''
Uses python 3.4.2
This class creates a prioritized list that the user and modify
'''
class PriorityList:
    '''
    Constructor: creates myList dictionary and saveFile
    Checks to see if the saveFile exists and imports it if it is found
    '''
    def __init__(self):
        #Dictionary containing item name, priority rating, and number of ratings
        self.myList = {}
        self.saveFile = 'list.etxt'

        try:
            #import list from list.etxt file
            with open(self.saveFile, 'r') as file:
                for line in file:
                    words = line.split('-')
                    name = words[0]
                    rating = words[1]
                    numOfRatings = words[2]
                    self.myList[name] = [rating, numOfRatings]
        except Exception as exc:
            #ignore file not found error
            print "Error: " + repr(exc)
            pass

    '''
    This method is used to add a new item with name and rating that is passed
    into this function to the priority list. Checks to see if name and
    rating have been entered. Calls self.save() to save file.
    '''
    def add(self, name, rating):
        #check to see if name is empty
        if name == "":
            print "No name was entered"
            return
        #check to see if rating is empty
        elif rating == "":
            print "No rating was entered"
            return
        else:
            self.myList[name] = [rating, 1]
        #save file
        self.save()

    '''
    This method is used to go through the list and update every item with a
    new rating. Will ask for new rating for given item. Calls self.save()
    to save the list to the file.
    '''
    def updateAllRatings(self):
        #Go through the list and rate each item
        for item, values in self.myList.items():
            #get new rating for item
            rating = float(raw_input("Enter new rating for %s from 1 to 10: " %(item)))
            #calculate new rating
            oldRating = float(values[0])
            numOfRatings = int(values[1]) + 1
            newRating = oldRating + ((rating - oldRating)/(numOfRatings))
            #update self.myList
            self.myList[item] = [newRating, numOfRatings]
        #save to file
        self.save()

    '''
    This method will ask for the name of an item and if it is in the list,
    it will ask for a rating and then update that item with the new rating.
    Updates rating based on average. 
    '''
    def updateOneRating(self):
        #update ratings based on given item        
        name = raw_input("Enter item for update: ")
        name = name.capitalize()
        newRating = 0
        #go through the list of items
        for item, values in self.myList.items():
            #if item equals given name
            if item == name:
                #get new rating from user
                try:
                    rating = float(raw_input("Enter new rating for %s from 1 to 10: " %(name)))
                except:
                    out("No rating was entered.")
                    return
                #calculate new rating
                oldRating = float(values[0])
                numOfRatings = int(values[1]) + 1
                newRating = oldRating + ((rating - oldRating)/(numOfRatings))
                #update self.myList
                self.myList[item] = [newRating, numOfRatings]
                self.save()
                return
                
        else:
            if name == "":
                print "No item was entered"
                return
            else:
                print "%s is not in the list." %(name)
                return
    '''
    This method with ask for an item to be removed. If the item is in the list,
    it will remove it from the list. Calls self.save() to save the file.
    '''
    def removeItem(self):
        name = raw_input("Enter item to be removed: ")
        name = name.capitalize()
        for item, values in self.myList.items():
            if item.capitalize() == name.capitalize():
                #remove item
                self.myList.pop(item)
                print "%s has been removed from the list" %(name)
                self.save()
                return
        else:
            if name == "":
                print "No item was entered"
            else:
                print "%s is not in the list." %(name)        

    '''
    This method with print out the priority list with the lowest rating first.
    '''
    def printList(self):
        #check to see if list is empty
        if not self.myList:
            print "There are no items in the list."
        else:
            print ""
            #create copy of priority list
            newList = self.myList.copy()
            #while there are items still in the newList
            while newList:
                name = ""
                rating = 1000.0
                #get lowest rating from newList
                for item, values in newList.items():
                    if float(values[0]) < float(rating):
                        rating = values[0]
                        name = item
                print "%s has a rating of %s" %(name, rating)
                #remove item from newList
                newList.pop(name)                
            print ""

    '''
    This method is used to save the priority list to the file. Prints out the
    error if the file fails to open, to write, or to close.
    '''
    def save(self):
        try:
            #overrite file with empty content
            file = open(self.saveFile, 'w')
            file.write("")
            file.close()
            #append priority list with all items
            with open(self.saveFile, "a") as file:
                #write myList to file
                for item, values in self.myList.items():
                    rating = values[0]
                    numOfRatings = int(str(values[1]).strip())
                    file.write("%s-%s-%s\n" %(item, rating, numOfRatings))
            print "List has been updated and saved"
        except Exception as ex:
            #do noting
            print "Save Error: " + repr(ex)
            pass

def menu():
    print "\n *****************************"
    print " *                           *"
    print " *  1)  Add Item             *"
    print " *  2)  View List            *"
    print " *  3)  Update Ratings       *"
    print " *  4)  Update Item          *"
    print " *  5)  Remove Item          *"
    print " *                           *"
    print " *  10) Close Program        *"
    print " *                           *"
    print " *****************************\n"

def main():
    #create PriorityList object
    myList = PriorityList()
    
    #run program until user closes it
    while True:
        menu()
        choice = 0
        try:
            choice = int(raw_input("Enter you choice: "))
        except Exception:
            #ignore invalid inputs
            pass
        if choice == 1:
            #get name and rating
            name = raw_input("Enter item name: ")
            rating = float(raw_input("Enter Rating from 1 to 10: "))
            #add item to myList
            myList.add(name.capitalize(), rating)
        elif choice == 2:
            myList.printList()
        elif choice == 3:
            myList.updateAllRatings()
        elif choice == 4:
            myList.updateOneRating()
        elif choice == 5:
            myList.removeItem()
        elif choice == 10:
            print "Closing program..."
            break
        else:
            print "Incorrect choice."

main()

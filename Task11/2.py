import os

class Writing :

    def __init__(self,filename,mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self) :
        self.open = open(self.filename,self.mode)
        print("File opened")
        return self.open

    def __exit__(self, exc_type, exc_value, traceback) :
            self.open.seek(0)
            self.text = self.open.read()

            if "bug" in self.text:
                self.open.close()
                os.remove(self.filename)
                print("Bug present, file removed")

            else :
                self.open.close()
                print("No bug present")
                print("File Closed")
try : 
    with Writing(r"C:\Users\ajuaj\Desktop\Beinex\Task11\text.txt","w+") as fp :

        fp.write("this is first line \n")
        fp.write("This is second line")

except Exception as e:
    print("Error", e)


        
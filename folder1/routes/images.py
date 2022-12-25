from fastapi import FastAPI,Response,status,HTTPException,Depends,APIRouter,Request
from fastapi.responses import FileResponse
import os
baseurl="http://localhost:8000"
def item(image,music):
    name,ext1=image.split('.')
    
    music,ext2=music.split(".")
    print(music,"music")
    music=music.replace(" ","%20")
    return{"name":name,"image_link":baseurl+f"/image/{name}?ext={ext1}","music":f"{baseurl}/music/{music}?ext=mp3"}
def file_giver(name):
  print("name",name)
 

  for root,dir,files in os.walk(f"D:\music\{name}"):
        print(files,"files")
        music=files[0:10]
        
  for root,dir,files in os.walk(f"D:\FastApi\images\{name}"):
        image=files
        print(music,image)
        new_item= list(map(item,image,music))
  return new_item



       
router=APIRouter()
@router.get("/details/artist/{name}")
def artist_image(name:str):
    print(name)
    ret_val= file_giver(name)
    if(name=="posty"):
     return ret_val
    elif(name=="one_republic"):
        return ret_val

@router.get('/image/{image_name}')
def images(image_name:str,ext:str):
    print((image_name))

    
    for root,dir,files in os.walk("D:\FastApi\images"):
        print("root is=",root)
        print("dir",dir)
        if f"{image_name}.{ext}" in files:
            file_name=os.path.join(root,image_name)
            return FileResponse(file_name+"."+ext)
        # else:
        #     return {'detail':"notfound"}    
    return FileResponse("D:\FastApi\images\posty\circle.jpg")

@router.get("/music/{music_name}")
def music(music_name:str,request:Request):
    
    # music_name=music_name.replace("%20"," ")
    print(music_name) 
    for root,dir,files in os.walk("D:\music"):
        print(root)
        print("in music ",files)
        if(music_name+".mp3" in files):
            ret=root+"\\"+music_name+".mp3"
            return FileResponse(ret)
        
    return{"found":False}   
    print (request.url)

    
#   for root,dir,files in os.walk(f"D:\music"):
#         if()


    
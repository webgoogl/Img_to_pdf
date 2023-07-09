from django.shortcuts import render,redirect
import img2pdf 
from django.conf import settings
import uuid

def pdf_converter(request):
    
    images=[]
    data={}
    i=0
    if request.method=='POST':
        obj=request.FILES.getlist('images')
        file_name=request.POST.get('file_name')
        if obj==None:
            return redirect('home.html')
        for img in obj:
            i+=1
            images.append(img)
        pdf=img2pdf.convert(images)
       
        fil=f'{file_name}'+f'{uuid.uuid4()}'
        file=open(f'media\\{fil}.pdf','wb')
        file.write(pdf)
        file.close()
        return render(request,'index.html',{'file':fil,'i':i})
       
       
       
    return render(request,'index.html')

# img=['bean.jpg','link.png']
# pdf=img2pdf.convert(img)

# file=open('D:\\MY FILES\\html programme\\file.pdf','wb')
# file.write(pdf)
# file.close()
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import item
from django.http import JsonResponse


def Homepage(request):
    sample=loader.get_template('mainpge.html')
    data={'category':'Appliances',
          'products':[
          {'ID':121,'Sub-categ.':'Phones','brand':'LG','feature':['16 gb ram']},
          {'ID':122,'Sub-categ.':'Phones','brand':'oppo','feature':['16 gb ram','1 TB','ssd']},
          {'ID':123,'Sub-categ.':'Television','brand':'samsung','feature':['42 inch size','image quality','audio capacity']},
          {'ID':124,'Sub-categ.':'Air conditioner','brand':'voltas','feature':['1.6 ton','split ac']},
          {'ID':125,'Sub-categ.':'washing machine','brand':'IFB','feature':['6 liter','fully automatic']}]}
    response=sample.render(data,request)
    return HttpResponse(response)

def Product(request,iid):
    template=loader.get_template('products.html')
    objects=item.objects.get(id=iid)
    data={'produts':objects}
    response=template.render(data,request)
    return HttpResponse(response)

def Product_data(req):
    template=loader.get_template('prod_dta.html')
    obj=item.objects.all()
    data={'items':obj}
    response=template.render(data,req)
    return HttpResponse(response)
'''
def addtocart(req):
    print(req)
    print(req.GET['proname'])
    print(req.GET['qty'])
    response = HttpResponse('add to cart successfully!!!')
    data = req.COOKIES.get('iid')

    if data != None:
         data= data +','+req.GET['proname']+'='+req.GET['qty']
    else:
        data=req.GET['proname']+'='+req.GET['qty']
    response.set_cookie('iid',data,60*60)
    return response

def viewcart(req):
    template=loader.get_template('shopping cart.html')
    data=req.COOKIES.get('iid')
    # items=data.split(',')
    # print(items)
    # data={}
    if data != None:
        items=data.split(',')
    #if items!=None:
        mycart=[]
        for item in items:
            values=item.split('=')
            proname=values[0]
            qty=values[1]
            mycart.append({proname:qty})
        data={'cart_data':mycart}
            # response=template.render(data,req)
    else:
        data={}
    response = template.render({},req)
    return HttpResponse(response)
'''

def addtocart(req):
    print(req)
    iid=req.GET['proname']
    qty=req.GET['qty']
    response=HttpResponse('Added to cart')
    cartitems={}
    if req.session.__contains__('cart_data'):
        cartitems=req.session['cart_data']
    cartitems[iid] = qty
    req.session['cart_data']=cartitems
    print(req.session['cart_data'])
    return HttpResponse(response)
'''
def viewcart(req):
    template=loader.get_template('shopping cart.html')
    #cartitems={}
    if req.session.__contains__('cart_data'):
        cartitems=req.session['cart_data']
        item_lists=[]
        for i,j in cartitems.items():
            prod_obj=item.objects.get(name=i)
            item_lists.append({'name':i,'qty':j,'price':prod_obj.price,'descri':prod_obj.descri,
                               'brand':prod_obj.brand,'total':prod_obj.price*int(j)})
            data={'pros':item_lists}
            res=template.render(data,req)
            return HttpResponse(res)
    else:
        return HttpResponse('Cart is empty') '''

def viewcart(req):
    template=loader.get_template('shopping cart.html')
    print(req.session.keys)
    if req.session.__contains__('cart_data'):
        for key in req.session.keys():
            print('Key:=>',req.session[key])
            items=list(req.session[key].items())
            itemlist=[]
        #print(len(items))
        #print(items[2])
        #key val=[]
            for i in range(len(items)):
                proname=items[i][0]
                qty=items[i][1]
               # print(proname,qty)
                prod_obj=item.objects.get(name=proname)
                itemlist.append({'name':proname,'qty':qty,
                                  'descri':prod_obj.descri,
                                  'price':prod_obj.price,
                                  'brand':prod_obj.brand,
                                  'total':prod_obj.price*int(qty)})
            data={'pros':itemlist}
            res=template.render(data,req)
            return HttpResponse(res)
    else:
        return HttpResponse('Cart is empty')

def getproducts(req):
    items=[]
    print(item.objects.all())
    for x in item.objects.all():
        items.append({'id':x.id,'name':x.name,'descri':x.descri,
                      'price':x.price,'brand':x.brand})
    data={'pros':items}
    return JsonResponse(data)

def getallproducts(req,key):
    items=[]
    print(key)
    for x in item.objects.filter(name__contains = key):
       # print(x.id,x.name)
        items.append({'id':x.id,'name':x.name,'descri':x.descri,
                      'price':x.price,'brand':x.brand})
    data={'pros':items}
    return JsonResponse(data)


def prodsearch(req):
    template=loader.get_template('allprods.html')
    data={}
    res=template.render(data,req)
    return HttpResponse(res)

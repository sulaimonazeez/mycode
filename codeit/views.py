from django.shortcuts import render

def home(request):
  return render(request, 'coder.html')
  
def basic_html(request):
  return render(request, 'html/basic.html')
  
def html_attr(request):
  return render(request, 'html/html-attr.html')
  
def html_element(request):
  return render(request, 'html/html-element.html')
def html_format(request):
  return render(request, 'html/html-formatting.html')
  
def html_heading(request):
  return render(request, 'html/html-heading.html')
def html_paragraph(request):
  return render(request, 'html/html-p.html')
  
def html_phrase(request):
  return render(request, 'html/html-phrase.html')
  
def html_anchor(request):
  return render(request, 'html/html-anchor.html')
  
def html_image(request):
  return render(request, "html/html-jmage.html")
  
def html_list(request):
  return render(request, 'html/html-list.html')
def html_order(request):
  return render(request, 'html/html-order.html')
  
def html_unorder(request):
  return render(request, 'html/html-unorder.html')
  
def html_description(request):
  return render(request, "html/html-describtion.html")
  
def html_form(request):
  return render(request, "html/html-form.html")
  
def html_input(request):
  return render(request, 'html/html-input.html')
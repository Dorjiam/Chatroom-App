from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound, Http404
from Message.models import Massage
from datetime import date

def chat(request, senderd, reciverd):


        todaydate = date.today()
        # "p" is short formof "part"
        p1_all = Massage.objects.filter(sender=reciverd, receiver=senderd)
        p2_all = Massage.objects.filter(sender=senderd, receiver=reciverd)

        p1_before_today = p1_all.exclude(date=todaydate.strftime("%Y-%m-%d"))
        p2_before_today = p2_all.exclude(date=todaydate.strftime("%Y-%m-%d"))
        before_today = p1_before_today.union(p2_before_today).order_by('date')

        p1_today = p1_all.filter(date=todaydate.strftime("%Y-%m-%d"))
        p2_today = p2_all.filter(date=todaydate.strftime("%Y-%m-%d"))
        today = p1_today.union(p2_today).order_by('date')

        yesterday = todaydate.strftime("%Y-%m-%d").split("-")
        if yesterday[2] != "01":
            yesterdayt = yesterday[0] + "-" + yesterday[1] + "-" + str(int(yesterday[2]) - 1)
        if yesterday[2] == "01":
            yesterdayt = yesterday[0] + "-" + str(int(yesterday[1]) - 1) + "-29"
        yesterday = p2_all.filter(date=yesterdayt)
        yesterdaytype = ""
        for i in yesterday:
            yesterdaytype = i.date
            break

        yesterday = todaydate.strftime("%Y-%m-%d").split("-")
        if yesterday[2] != "01":
            yesterdayt = yesterday[0] + "-" + yesterday[1] + "-" + str(int(yesterday[2]) - 1)
        if yesterday[2] == "01":
            yesterdayt = yesterday[0] + "-" + str(int(yesterday[1]) - 1) + "-29"
        yesterday = p1_all.filter(date=yesterdayt)
        yesterdaytype2 = ""
        for i in yesterday:
            yesterdaytype2 = i.date
            break

        text = ""
        for i in p2_all:
            text = i.sender
            break

        p_k_ = None
        listpk = []
        for i in before_today:
            if i.date != p_k_:
                listpk.append(i.pk)
                p_k_ = i.date

        if len(today) == 0 and len(before_today) == 0:
            return render(request, "nothing.html")
        else:
            today_line = True
            if len(today) == 0:
                today_line = False
            chatdir = {
                'reciver' : reciverd,
                'sender' : senderd,
                'today': today,
                'all': before_today,
                'sender_key': text,
                'pk_list': listpk,
                'today_line': today_line,
                'yesterday': yesterdaytype,
                'yesterday2': yesterdaytype2
            }
            return render(request, "chat.html", context=chatdir)

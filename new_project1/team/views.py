from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status
from .models import Member,Team,BillMember
from user.models import User
from .serializer import MemberSerializer,TeamSerializer
from datetime import datetime
from pytz import timezone
from django.http import HttpResponseBadRequest


class MemberView(APIView):
    def get_object(self, pk):
        try:
            return Member.objects.get(pk=pk)
        except Member.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        id = self.get_object(pk)
        serializer = MemberSerializer(id)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        instance = self.get_object(pk)
        serializer = MemberSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk, format=None):
        val = self.get_object(pk)
        val.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class MemberViewList(APIView):
    def get(self, request, format=None):
        data = Member.objects.all()
        serializer = MemberSerializer(data, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = MemberSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class TeamView(APIView):
    def get_object(self, pk):
        try:
            return Team.objects.get(pk=pk)
        except Team.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        id = self.get_object(pk)
        serializer = TeamSerializer(id)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        instance = self.get_object(pk)
        serializer = TeamSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk, format=None):
        val = self.get_object(pk)
        val.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class TeamViewList(APIView):
    def get(self, request, format=None):
        data = Team.objects.all()
        serializer = TeamSerializer(data, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TeamSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class GetAllTeamMembers(APIView):
    def get(self,request, format= None,):
        team_id = self.request.query_params.get('team_id')

        if team_id is not None:
            team = Member.objects.filter(t_name=team_id).values('id','member__name','member__email','member')
            return Response(team, status=status.HTTP_200_OK)
        return Response("Team id not found", status=status.HTTP_204_NO_CONTENT)
    
    def post(self, request, format=None):
        t_name_id = request.data.get('t_name')
        member_id = request.data.get('members')
        created_at = datetime.now(timezone('UTC'))
        print(t_name_id)
        print(member_id)
        
        if t_name_id and member_id:
            t_name = Team.objects.get(id=t_name_id)
            member = User.objects.get(id=member_id)
            print(t_name)
            print(member)
            
            member_data = Member.objects.create(
                t_name=t_name,
                member=member,
                created_at=created_at
            )
            print(member_data)

            return Response("member created", status=status.HTTP_201_CREATED)
        else:
            return Response('t_name and member are required', status=status.HTTP_400_BAD_REQUEST)   

        
    def put(self, request, format=None):
        member_id = request.query_params.get('member_id')
        # import pdb
        # pdb.set_trace()
        try:
            team = Member.objects.get(id=member_id)
            print(team)
            team.t_name.id = request.data.get("t_name")
            team.created_at = datetime.now(timezone('UTC'))
            team.save()
            return Response("Successfully Updated",status=status.HTTP_200_OK)
        except Member.DoesNotExist:
            return HttpResponseBadRequest("Member does not exist")


class NextBillPayerView(APIView):
    def get_next_bill_payer(self):
        next_member = BillMember.objects.order_by('position').filter(payment_status=False).first()
        return next_member
    
    def get(self, request, format=None):
        next_bill_payer = self.get_next_bill_payer()
        print(next_bill_payer)

        if not next_bill_payer: 
            BillMember.objects.all().update(payment_status=False)
            next_bill_payer = self.get_next_bill_payer()

        next_bill_payer.payment_status = True
        next_bill_payer.save()  
        return Response("Bill assigned successfully", status=status.HTTP_200_OK)

# class NextBillPayerView(APIView):
    # def get_next_bill_payer(self):
    #     next_order = BillMember.objects.order_by('id').filter(payment_status=False).first()
    #     return next_order

    # def get(self, request, bill_member_id, format=None):
    #     try:
    #         bill_member = BillMember.objects.get(id=bill_member_id)
    #     except BillMember.DoesNotExist:
    #         return Response("Invalid bill member ID")

    #     next_bill_payer = self.get_next_bill_payer()
    #     if bill_member != next_bill_payer:
    #         return Response("This member is not the next bill payer")

    #     bill_member.payment_status = True
    #     bill_member.save()

    #     return Response("Payment status updated successfully")





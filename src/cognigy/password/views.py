import string
import random
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers


class PasswordSerializer(serializers.Serializer):
    min_length = serializers.IntegerField()
    special_char = serializers.IntegerField()
    number_of_numbers = serializers.IntegerField()
    number_of_passwords = serializers.IntegerField()

class ApiGeneratePassword(viewsets.ModelViewSet):
    """ API endpoint that generate secure passwords:

        The user must insert the following fields:
        - minimum length
        - the number of special characters
        - the number of numbers and
        - the number of passwords that shall be created.
    """
    serializer_class = PasswordSerializer

    def genrate_password(self, request, *args, **kwargs):
        if not request.data:
            return Response({'detail': 'Bad request, please fill in all the required fields'},
                            status=status.HTTP_400_BAD_REQUEST)
                            
        if request.data.get('min_length') == '' or \
           request.data.get('special_char') == '' or \
           request.data.get('number_of_numbers') == '' or \
           request.data.get('number_of_passwords') == '':

            return Response({'detail': 'Bad request, please fill in all the required fields'},
                            status=status.HTTP_400_BAD_REQUEST)
        passwords = []

        min_length = int(request.data.get('min_length'))
        number_of_special_char = int(request.data.get('special_char'))
        number_of_numbers = int(request.data.get('number_of_numbers'))
        number_of_passwords = int(request.data.get('number_of_passwords'))

        letters = string.ascii_letters
        digits = string.digits
        special_char = string.punctuation

        for i in range(number_of_passwords):
            password = random.choices(special_char, k=number_of_special_char)
            password += random.choices(digits, k=number_of_numbers)
            password += random.choices(letters, k=min_length -
                                       (number_of_numbers+number_of_special_char))

            random.SystemRandom().shuffle(password)
            password = ''.join(password)

            passwords.append(password)

        return Response({'passwords': passwords}, status=status.HTTP_200_OK)

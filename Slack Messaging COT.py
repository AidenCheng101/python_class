# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 10:01:55 2021

@author: fcheng
"""
from slacker import Slacker

slack =Slacker('xoxb-601281740211-1247053430977-377GzutS7JrDYqAkg6fqMlwr')
channel = 'coffee-rv'

slack.chat.post_message(channel, attachments = [{"text": "Robusta COT Update: <https://app.powerbi.com/groups/me/apps/945dd6c7-0284-4300-97db-8590e7377424/dashboards/61a446b7-8a7e-4ec4-8f4e-9a8ff0d12b8c?ctid=91fd65df-e972-4197-96fb-0d3f5b16c098|Link to BI Dashboard>"}],
                            username='Alert',
                            icon_emoji=':male-firefighter:')

slack.chat.post_message(channel, attachments = [{"text": "Arabica COT Update: <https://app.powerbi.com/groups/me/apps/945dd6c7-0284-4300-97db-8590e7377424/dashboards/6a18a4d1-f2ae-4d78-8be5-ae32229ebf5f?ctid=91fd65df-e972-4197-96fb-0d3f5b16c098|Link to BI Dashboard>"}],
                            username='Alert',
                            icon_emoji=':male-firefighter:')




#slack.files.upload('C:/Users/fcheng/Desktop/table3.png', title='Grading', initial_comment='Big jump', channels=channel)

slack.chat.post_message(channel, attachments = [{"text": "Arabica Certs Update (with New Aging Report): <https://app.powerbi.com/groups/me/apps/945dd6c7-0284-4300-97db-8590e7377424/dashboards/02cf530b-3d6e-4103-96e9-4079a494c7a6?ctid=91fd65df-e972-4197-96fb-0d3f5b16c098|Link to BI Dashboard>"}],
                            username='Alert',
                            icon_emoji=':male-firefighter:')


slack.chat.post_message(channel, attachments = [{"text": "US Coffee Imports New Data Alert: More details to follow..."}],
                            username='Alert',
                            icon_emoji=':male-firefighter:')

slack.chat.post_message(channel, attachments = [{"text": "US Coffee Imports Update: <https://app.powerbi.com/groups/me/apps/945dd6c7-0284-4300-97db-8590e7377424/dashboards/02cf530b-3d6e-4103-96e9-4079a494c7a6?ctid=91fd65df-e972-4197-96fb-0d3f5b16c098|Link to BI Dashboard>"}],
                            username='Alert',
                            icon_emoji=':male-firefighter:')
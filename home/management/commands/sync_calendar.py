#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""sync_hall_calendar --

"""
import pathlib
import datetime

from django.core.management import BaseCommand
from simple_google_calendar_reader import SimpleGoogleCalendarReader
from home.models.hall_event_model import HallEventModel
from home.models.garbage_event_model import GarbageEventModel
from home.models.main_event_model import MainEventModel


EVENT_CONFIRMED_STATUS = 1
EVENT_TENTATIVE_STATUS = 2
EVENT_CANCELLED_STATUS = 3

EVENT_STATUS = ((EVENT_CONFIRMED_STATUS, 'confirmed'),
                (EVENT_TENTATIVE_STATUS, 'tentative'),
                (EVENT_CANCELLED_STATUS, 'cancelled'), )

EVENT_STATUS_DICT = {x[1]: x[0] for x in EVENT_STATUS}


class Command(BaseCommand):
    """Command

    Command is a BaseCommand.
    Responsibility:
    """
    help = 'Syncronize Google Calendars.'

    # TOKEN
    TOKEN_PATH = pathlib.Path(__file__).parent.joinpath('token.json')
    SECRET_PATH =  pathlib.Path(__file__).parent.joinpath('client_secret.json')

    MAX_RESULTS = 200

    class CalendarID(object):
        """CalendarID

        CalendarID is a object.
        Responsibility:
        """
        MAIN = 'satotanakami@gmail.com'
        HALL = '6m5ne5kcfmkek4t0ba37o95olo@group.calendar.google.com'
        GARBAGE = 'c9uc1q8uiftrf0agsvvbpo6dvc@group.calendar.google.com'

    def add_arguments(self, parser):
        """SUMMARY

        add_arguments(parser)

        @Arguments:
        - `parser`:

        @Return:

        @Error:
        """
        parser.add_argument('-m', '--main',
                            dest='main',
                            action='store_true',
                            default=False,
                            help='Sync with main calendar.')
        parser.add_argument('-g', '--garbage',
                            dest='garbage',
                            action='store_true',
                            default=False,
                            help='Sync with garbage calendar.')
        parser.add_argument('-l', '--hall',
                            dest='hall',
                            action='store_true',
                            default=False,
                            help='Sync with hall calendar.')

    def sync_main_calendar(self, ):
        """SUMMARY

        sync_main_calendar()

        @Return:

        @Error:
        """
        calendar_reader = SimpleGoogleCalendarReader(self.TOKEN_PATH, self.SECRET_PATH, self.CalendarID.MAIN)
        now = datetime.datetime.now(datetime.timezone.utc)
        # タイムゾーンフォーマットを削除 2025-01-25T11:27:12.772273+00:00Z => 2025-01-25T11:27:12.772343Z
        now = now.replace(tzinfo=None)
        before_day = now - datetime.timedelta(days=2)
        before_day_string = before_day.isoformat() + "Z"
        events = calendar_reader.read(before_day_string, max_results=self.MAX_RESULTS)
        for event in events:
            defaults = {}
            defaults['gid'] = event['id']
            defaults['summary'] = event.get('summary', '')
            defaults['description'] = event.get('description', '')
            defaults['url'] = event['htmlLink']
            try:
                defaults['created'] = datetime.datetime.fromisoformat(event['created'])
            except ValueError as err:
                defaults['created'] = datetime.datetime.now()
            try:
                defaults['modified'] = datetime.datetime.fromisoformat(event['updated'])
            except ValueError as err:
                defaults['modified'] = datetime.datetime.now()
            defaults['status'] = EVENT_STATUS_DICT.get(
                event['status'], EVENT_CANCELLED_STATUS)
            if 'start' in event and 'date' in event['start']:
                start = datetime.datetime.strptime(event['start']['date'], '%Y-%m-%d')
                defaults['start'] = start
                defaults['end'] = datetime.datetime.combine(start, datetime.time.max)
            else:
                defaults['start'] = datetime.datetime.fromisoformat(event['start']['dateTime'])
                defaults['end'] = datetime.datetime.fromisoformat(event['end']['dateTime'])
            model, created = MainEventModel.objects.get_or_create(gid=event['id'], defaults=defaults)
            if created:
                continue
            model.gid = defaults['gid']
            model.summary = defaults['summary']
            model.description = defaults['description']
            model.start = defaults['start']
            model.end = defaults['end']
            model.url = defaults['url']
            model.created = defaults['created']
            model.modified = defaults['modified']
            model.status = defaults['status']
            model.save()

    def sync_hall_calendar(self, ):
        """SUMMARY

        sync_hall_calendar()

        @Return:

        @Error:
        """
        calendar_reader = SimpleGoogleCalendarReader(self.TOKEN_PATH, self.SECRET_PATH, self.CalendarID.HALL)
        now = datetime.datetime.now(datetime.timezone.utc)
        # タイムゾーンフォーマットを削除 2025-01-25T11:27:12.772273+00:00Z => 2025-01-25T11:27:12.772343Z
        now = now.replace(tzinfo=None)
        before_day = now - datetime.timedelta(days=2)
        before_day_string = before_day.isoformat() + "Z"
        events = calendar_reader.read(before_day_string, max_results=self.MAX_RESULTS)
        for event in events:
            defaults = {}
            defaults['gid'] = event['id']
            defaults['summary'] = event.get('summary', '')
            defaults['description'] = event.get('description', '')
            defaults['url'] = event['htmlLink']
            try:
                defaults['created'] = datetime.datetime.fromisoformat(event['created'])
            except ValueError as err:
                defaults['created'] = datetime.datetime.now()
            try:
                defaults['modified'] = datetime.datetime.fromisoformat(event['updated'])
            except ValueError as err:
                defaults['modified'] = datetime.datetime.now()
            defaults['status'] = EVENT_STATUS_DICT.get(
                event['status'], EVENT_CANCELLED_STATUS)
            if 'start' in event and 'date' in event['start']:
                start = datetime.datetime.strptime(event['start']['date'], '%Y-%m-%d')
                defaults['start'] = start
                defaults['end'] = datetime.datetime.combine(start, datetime.time.max)
            else:
                defaults['start'] = datetime.datetime.fromisoformat(event['start']['dateTime'])
                defaults['end'] = datetime.datetime.fromisoformat(event['end']['dateTime'])

            model, created = HallEventModel.objects.get_or_create(gid=event['id'], defaults=defaults)
            if created:
                continue
            model.gid = defaults['gid']
            model.summary = defaults['summary']
            model.description = defaults['description']
            model.start = defaults['start']
            model.end = defaults['end']
            model.url = defaults['url']
            model.created = defaults['created']
            model.modified = defaults['modified']
            model.status = defaults['status']
            model.save()

    def sync_garbage_calendar(self, ):
        calendar_reader = SimpleGoogleCalendarReader(self.TOKEN_PATH, self.SECRET_PATH, self.CalendarID.GARBAGE)
        now = datetime.datetime.now(datetime.timezone.utc)
        now = now.replace(tzinfo=None).isoformat() + "Z"
        events = calendar_reader.read(now, max_results=self.MAX_RESULTS)
        for event in events:
            defaults = {}
            defaults['gid'] = event['id']
            defaults['summary'] = event.get('summary', '')
            defaults['date'] = datetime.datetime.strptime(
                event['start']['date'], '%Y-%m-%d').date()
            defaults['status'] = EVENT_STATUS_DICT.get(
                event['status'], EVENT_CANCELLED_STATUS)
            model, created = GarbageEventModel.objects.get_or_create(
                gid=event['id'], defaults=defaults)
            if created:
                continue
            model.gid = defaults['gid']
            model.summary = defaults['summary']
            model.date = defaults['date']
            model.url = defaults['url']
            model.status = defaults['status']
            model.save()

    def handle(self, *args, **options):
        if options['main'] == True:
            self.sync_main_calendar()
        if options['hall'] == True:
            self.sync_hall_calendar()
        if options['garbage'] == True:
            self.sync_garbage_calendar()



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# sync_hall_calendar.py ends here

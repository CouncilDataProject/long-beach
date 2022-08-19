#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime
from typing import List

from cdp_backend.pipeline.ingestion_models import EventIngestionModel
from cdp_scrapers.legistar_utils import LegistarScraper

###############################################################################


def get_events(
    from_dt: datetime,
    to_dt: datetime,
    **kwargs,
) -> List[EventIngestionModel]:
    scraper = LegistarScraper(
        client="longbeach",
        timezone="America/Los_Angeles",
        ignore_minutes_item_patterns=[
            "VIA TELECONFERENCE PURSUANT TO AB 361",
            "certify that the agenda was posted not less than 72 hours",
            "The agenda and supporting documents are available on the Internet",
            "IN-PERSON/VIRTUAL HYBRID CITY COUNCIL MEETING",
            "PURSUANT TO AB 361",
            "Opportunity to address the City Council",
            "VIA TELECONFERENCE",
            "JOIN VIA ZOOM",
            "TO PROVIDE PUBLIC COMMENT IN THE ZOOM MEETING",
            "NOTICE TO THE PUBLIC",
            "Opportunity is given to those members of the public",
            "page break",
            "REVISED",
            "PAGE BREAK",
        ],
    )

    return scraper.get_events(begin=from_dt, end=to_dt)

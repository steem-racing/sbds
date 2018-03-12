# -*- coding: utf-8 -*-

import dateutil.parser
import rapidjson

from sqlalchemy import DateTime
from sqlalchemy import String
from sqlalchemy import Column
from sqlalchemy import Numeric
from sqlalchemy import Unicode
from sqlalchemy import UnicodeText
from sqlalchemy import Boolean
from sqlalchemy import SmallInteger
from sqlalchemy import Integer
from sqlalchemy import BigInteger
from sqlalchemy import ForeignKey

from sqlalchemy.dialects.postgresql import JSONB

from ..import Base
from ...enums import operation_types_enum
from ...field_handlers import json_string_field
from ...field_handlers import amount_field
from ...field_handlers import amount_symbol_field
from ...field_handlers import comment_body_field
from .base import BaseOperation
from .base import BaseVirtualOperation

class ReportOverProductionOperation(Base, BaseOperation):
    """


    Steem Blockchain Example
    ======================




    """

    __tablename__ = 'sbds_op_report_over_productions'
    __operation_type__ = 'report_over_production_operation'

    reporter = Column(String(16), ForeignKey("sbds_meta_accounts.name")) # steem_type:account_name_type
    first_block = Column(JSONB) # steem_type:signed_block_header
    second_block = Column(JSONB) # steem_type:signed_block_header
    operation_type = Column(
        operation_types_enum,
        nullable=False,
        index=True,
        default='report_over_production')

    _fields = dict(
        first_block=lambda x:json_string_field(x.get('first_block')), # steem_type:signed_block_header
        second_block=lambda x:json_string_field(x.get('second_block')), # steem_type:signed_block_header
    )



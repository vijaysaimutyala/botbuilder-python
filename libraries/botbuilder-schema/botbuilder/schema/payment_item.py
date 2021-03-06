# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class PaymentItem(Model):
    """Indicates what the payment request is for and the value asked for.

    :param label: Human-readable description of the item
    :type label: str
    :param amount: Monetary amount for the item
    :type amount: ~botframework.connector.models.PaymentCurrencyAmount
    :param pending: When set to true this flag means that the amount field is
     not final.
    :type pending: bool
    """

    _attribute_map = {
        'label': {'key': 'label', 'type': 'str'},
        'amount': {'key': 'amount', 'type': 'PaymentCurrencyAmount'},
        'pending': {'key': 'pending', 'type': 'bool'},
    }

    def __init__(self, **kwargs):
        super(PaymentItem, self).__init__(**kwargs)
        self.label = kwargs.get('label', None)
        self.amount = kwargs.get('amount', None)
        self.pending = kwargs.get('pending', None)

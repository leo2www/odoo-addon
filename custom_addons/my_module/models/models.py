from odoo import models, fields
from datetime import timedelta

class TestModel(models.Model):
    _name = 'estate.property'
    _description = '测试模型'

    active = fields.Boolean(
        string='活动',
        default=False
        )

    name = fields.Char(
        string='名称', # UI 标签
        required=True, # 必填
        help='The name of the property', # 帮助文本
        default='未命名'
        )
    last_seen = fields.Datetime(
        string='最后看到',
        default=lambda self: fields.Datetime.now()
        )
    description = fields.Text(string='描述')
    postcode = fields.Char(string='邮编')
    date_availability = fields.Date(
            # Start of Selection
            string='可用日期', 
            copy=False,
            default=lambda self: fields.Date.today() + timedelta(days=90)
            )
    expected_price = fields.Float(
        string='预期价格',
        required=True
        )
    selling_price = fields.Float(
            # Start of Selection
            string='销售价格',
            readonly=True,
            copy=False
            )
    bedrooms = fields.Integer(
            # Start of Selection
            string='卧室数量', 
            default=2
            )
    living_area = fields.Float(string='居住面积')
    garden_area = fields.Float(string='花园面积')
    garden_orientation = fields.Selection([('north', '北'), ('south', '南'), ('east', '东'), ('west', '西')], string='花园方向')

    state = fields.Selection(
        selection=[
            ('new', 'New'),
            ('offer_received', 'Offer Received'),
            ('offer_accepted', 'Offer Accepted'),
            ('sold', 'Sold'),
            ('cancelled', 'Cancelled'),
        ],
        string='销售状态',
        required=True,
        copy=False,
        default='new'
    )

    def toggle_active(self):
        for record in self:
            record.active = not record.active


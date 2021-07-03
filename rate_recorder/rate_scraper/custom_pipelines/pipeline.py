"""
Using this pipeline to dump data in SQL and eventually use in Django.
"""


class RateRecorderPipeline(object):
    def process_item(self, item, spider):
        item.save()
        return item

# model settings
model = dict(
    type='ImageClassifier',
    backbone=dict(type='MobileNetV2', widen_factor=1.0),
    neck=dict(type='GlobalAveragePooling'),
    head=dict(
        type='MultiTaskHead',
        task_heads={
            'indoor': dict(type='LinearClsHead', num_classes=67),
            'intel': dict(type='LinearClsHead', num_classes=6),
        },
        in_channels=1280,
        loss=dict(type='CrossEntropyLoss', loss_weight=1.0),
    ))

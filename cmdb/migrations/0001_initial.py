# Generated by Django 2.1.2 on 2018-11-04 17:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cabinet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='机柜')),
                ('desc', models.CharField(blank=True, max_length=100, verbose_name='描述')),
            ],
        ),
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostname', models.CharField(max_length=50, unique=True, verbose_name='主机名')),
                ('ip', models.GenericIPAddressField(verbose_name='内网IP')),
                ('other_ip', models.CharField(blank=True, max_length=15, verbose_name='外网IP')),
                ('asset_no', models.CharField(blank=True, max_length=50, verbose_name='资产编号')),
                ('asset_type', models.CharField(blank=True, choices=[('1', '物理机'), ('2', '虚拟机'), ('3', '容器'), ('4', '网络设备'), ('5', '安全设备'), ('6', 'ECS'), ('7', 'RDS'), ('8', '其他')], max_length=30, null=True, verbose_name='设备类型')),
                ('status', models.CharField(blank=True, choices=[('1', 'online'), ('2', '闲置'), ('3', '可回收'), ('4', '其它')], max_length=30, null=True, verbose_name='设备状态')),
                ('os', models.CharField(blank=True, max_length=100, verbose_name='操作系统')),
                ('vendor', models.CharField(blank=True, max_length=50, verbose_name='设备厂商')),
                ('up_time', models.CharField(blank=True, max_length=50, verbose_name='上架时间')),
                ('cpu_model', models.CharField(blank=True, max_length=100, verbose_name='CPU型号')),
                ('cpu_num', models.CharField(blank=True, max_length=100, verbose_name='CPU数量')),
                ('memory', models.CharField(blank=True, max_length=30, verbose_name='内存大小')),
                ('disk', models.CharField(blank=True, max_length=255, verbose_name='硬盘信息')),
                ('sn', models.CharField(blank=True, max_length=60, verbose_name='SN号 码')),
                ('position', models.CharField(blank=True, max_length=100, verbose_name='所在位置')),
                ('memo', models.TextField(blank=True, max_length=200, verbose_name='备注信息')),
            ],
        ),
        migrations.CreateModel(
            name='HostGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True, verbose_name='服务器组名')),
                ('desc', models.CharField(blank=True, max_length=100, verbose_name='描述')),
                ('serverList', models.ManyToManyField(blank=True, to='cmdb.Host', verbose_name='所在服务器')),
            ],
        ),
        migrations.CreateModel(
            name='Idc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ids', models.CharField(max_length=255, unique=True, verbose_name='机房标识')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='机房名称')),
                ('address', models.CharField(blank=True, max_length=100, verbose_name='机房地址')),
                ('tel', models.CharField(blank=True, max_length=30, verbose_name='机房电话')),
                ('contact', models.CharField(blank=True, max_length=30, verbose_name='客户经理')),
                ('contact_phone', models.CharField(blank=True, max_length=30, verbose_name='移动电话')),
                ('jigui', models.CharField(blank=True, max_length=30, verbose_name='机柜信息')),
                ('ip_range', models.CharField(blank=True, max_length=30, verbose_name='IP范围')),
                ('bandwidth', models.CharField(blank=True, max_length=30, verbose_name='接入带宽')),
                ('memo', models.TextField(blank=True, max_length=200, verbose_name='备注信息')),
            ],
            options={
                'verbose_name': '数据中心',
                'verbose_name_plural': '数据中心',
            },
        ),
        migrations.CreateModel(
            name='InterFace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('vendor', models.CharField(max_length=30, null=True)),
                ('bandwidth', models.CharField(max_length=30, null=True)),
                ('tel', models.CharField(max_length=30, null=True)),
                ('contact', models.CharField(max_length=30, null=True)),
                ('startdate', models.DateField()),
                ('enddate', models.DateField()),
                ('price', models.IntegerField(verbose_name='价格')),
            ],
        ),
        migrations.CreateModel(
            name='IpSource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('net', models.CharField(max_length=30)),
                ('subnet', models.CharField(max_length=30, null=True)),
                ('describe', models.CharField(max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30, null=True)),
                ('password', models.CharField(max_length=30, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='host',
            name='idc',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cmdb.Idc', verbose_name='所在机房'),
        ),
        migrations.AddField(
            model_name='cabinet',
            name='idc',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cmdb.Idc', verbose_name='所在机房'),
        ),
        migrations.AddField(
            model_name='cabinet',
            name='serverList',
            field=models.ManyToManyField(blank=True, to='cmdb.Host', verbose_name='所在服务器'),
        ),
    ]
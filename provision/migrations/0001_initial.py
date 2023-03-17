# Generated by Django 4.0.4 on 2023-03-17 19:13

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('tenants', '0003_alter_defaultsetting_enabled_alter_domain_enabled_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeviceProfiles',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='Profile')),
                ('name', models.CharField(max_length=64, verbose_name='Name')),
                ('enabled', models.CharField(blank=True, choices=[('false', 'False'), ('true', 'True')], default='true', max_length=8, verbose_name='Enabled')),
                ('description', models.CharField(blank=True, max_length=254, null=True, verbose_name='Description')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, null=True, verbose_name='Updated')),
                ('synchronised', models.DateTimeField(blank=True, null=True, verbose_name='Synchronised')),
                ('updated_by', models.CharField(max_length=64, verbose_name='Updated by')),
                ('domain_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tenants.domain', verbose_name='Domain')),
            ],
            options={
                'db_table': 'pbx_device_profiles',
            },
        ),
        migrations.CreateModel(
            name='Devices',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='Device')),
                ('mac_address', models.CharField(max_length=24, verbose_name='MAC Address')),
                ('label', models.CharField(blank=True, max_length=64, null=True, verbose_name='Label')),
                ('model', models.CharField(blank=True, max_length=64, null=True, verbose_name='Model')),
                ('firmware_version', models.CharField(blank=True, max_length=64, null=True, verbose_name='Firmware Version')),
                ('template', models.CharField(blank=True, max_length=254, null=True, verbose_name='Template')),
                ('username', models.CharField(blank=True, max_length=32, null=True, verbose_name='Username')),
                ('password', models.CharField(blank=True, max_length=32, null=True, verbose_name='Password')),
                ('provisioned_date', models.DateTimeField(blank=True, null=True, verbose_name='Provisioned Date')),
                ('provisioned_method', models.CharField(blank=True, max_length=16, null=True, verbose_name='Prov. Method')),
                ('enabled', models.CharField(blank=True, choices=[('false', 'False'), ('true', 'True')], default='true', max_length=8, verbose_name='Enabled')),
                ('description', models.CharField(blank=True, max_length=254, null=True, verbose_name='Description')),
                ('provisioned_ip', models.GenericIPAddressField(unique=True, verbose_name='Provisioned Address')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, null=True, verbose_name='Updated')),
                ('synchronised', models.DateTimeField(blank=True, null=True, verbose_name='Synchronised')),
                ('updated_by', models.CharField(max_length=64, verbose_name='Updated by')),
                ('domain_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tenants.domain', verbose_name='Domain')),
                ('profile_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='provision.deviceprofiles', verbose_name='Profile')),
                ('user_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tenants.profile', verbose_name='User')),
            ],
            options={
                'db_table': 'pbx_devices',
            },
        ),
        migrations.CreateModel(
            name='DeviceVendors',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='Vendor')),
                ('name', models.CharField(max_length=64, verbose_name='Name')),
                ('enabled', models.CharField(blank=True, choices=[('false', 'False'), ('true', 'True')], default='true', max_length=8, verbose_name='Enabled')),
                ('description', models.CharField(blank=True, max_length=254, null=True, verbose_name='Description')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, null=True, verbose_name='Updated')),
                ('synchronised', models.DateTimeField(blank=True, null=True, verbose_name='Synchronised')),
                ('updated_by', models.CharField(max_length=64, verbose_name='Updated by')),
            ],
            options={
                'db_table': 'pbx_device_vendors',
            },
        ),
        migrations.CreateModel(
            name='DeviceVendorFunctions',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='Function')),
                ('name', models.CharField(max_length=64, verbose_name='Name')),
                ('value', models.CharField(blank=True, max_length=254, null=True, verbose_name='Value')),
                ('enabled', models.CharField(blank=True, choices=[('false', 'False'), ('true', 'True')], default='true', max_length=8, verbose_name='Enabled')),
                ('description', models.CharField(blank=True, max_length=254, null=True, verbose_name='Description')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, null=True, verbose_name='Updated')),
                ('synchronised', models.DateTimeField(blank=True, null=True, verbose_name='Synchronised')),
                ('updated_by', models.CharField(max_length=64, verbose_name='Updated by')),
                ('vendor_id', models.ForeignKey(db_column='vendor_id', on_delete=django.db.models.deletion.CASCADE, to='provision.devicevendors', verbose_name='Vendor')),
            ],
            options={
                'db_table': 'pbx_device_vendor_functions',
            },
        ),
        migrations.CreateModel(
            name='DeviceVendorFunctionGroups',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='Function')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, null=True, verbose_name='Updated')),
                ('synchronised', models.DateTimeField(blank=True, null=True, verbose_name='Synchronised')),
                ('updated_by', models.CharField(max_length=64, verbose_name='Updated by')),
                ('function_id', models.ForeignKey(db_column='function_id', on_delete=django.db.models.deletion.CASCADE, to='provision.devicevendorfunctions', verbose_name='Function')),
                ('group_id', models.ForeignKey(db_column='group_id', on_delete=django.db.models.deletion.CASCADE, to='auth.group', verbose_name='Group')),
            ],
            options={
                'db_table': 'pbx_device_vendor_function_groups',
            },
        ),
        migrations.CreateModel(
            name='DeviceSettings',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='Setting')),
                ('name', models.CharField(max_length=64, verbose_name='Name')),
                ('value', models.CharField(blank=True, max_length=254, null=True, verbose_name='Value')),
                ('enabled', models.CharField(blank=True, choices=[('false', 'False'), ('true', 'True')], default='true', max_length=8, verbose_name='Enabled')),
                ('description', models.CharField(blank=True, max_length=254, null=True, verbose_name='Description')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, null=True, verbose_name='Updated')),
                ('synchronised', models.DateTimeField(blank=True, null=True, verbose_name='Synchronised')),
                ('updated_by', models.CharField(max_length=64, verbose_name='Updated by')),
                ('device_id', models.ForeignKey(db_column='device_id', on_delete=django.db.models.deletion.CASCADE, to='provision.devices', verbose_name='Device')),
            ],
            options={
                'db_table': 'pbx_device_settings',
            },
        ),
        migrations.AddField(
            model_name='devices',
            name='vendor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='provision.devicevendors', verbose_name='Vendor'),
        ),
        migrations.CreateModel(
            name='DeviceProfileSettings',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='Setting')),
                ('name', models.CharField(max_length=64, verbose_name='Name')),
                ('value', models.CharField(blank=True, max_length=254, null=True, verbose_name='Value')),
                ('enabled', models.CharField(blank=True, choices=[('false', 'False'), ('true', 'True')], default='true', max_length=8, verbose_name='Enabled')),
                ('description', models.CharField(blank=True, max_length=254, null=True, verbose_name='Description')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, null=True, verbose_name='Updated')),
                ('synchronised', models.DateTimeField(blank=True, null=True, verbose_name='Synchronised')),
                ('updated_by', models.CharField(max_length=64, verbose_name='Updated by')),
                ('device_id', models.ForeignKey(db_column='device_id', on_delete=django.db.models.deletion.CASCADE, to='provision.devices', verbose_name='Device')),
            ],
            options={
                'db_table': 'pbx_device_profile_settings',
            },
        ),
        migrations.CreateModel(
            name='DeviceProfileKeys',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='Key')),
                ('category', models.CharField(blank=True, choices=[('', 'Not Set'), ('line', 'Line'), ('memory', 'Memory'), ('programmable', 'Programmable'), ('expansion-1', 'Expansion 1'), ('expansion-2', 'Expansion 2'), ('expansion-3', 'Expansion 3'), ('expansion-4', 'Expansion 4'), ('expansion-5', 'Expansion 5'), ('expansion-6', 'Expansion 6')], default='line', max_length=16, verbose_name='Category')),
                ('key_id', models.DecimalField(decimal_places=0, default=1, max_digits=11, verbose_name='Key')),
                ('key_type', models.CharField(max_length=64, verbose_name='Key type')),
                ('line', models.DecimalField(decimal_places=0, default=1, max_digits=3, verbose_name='Line')),
                ('value', models.CharField(blank=True, max_length=254, null=True, verbose_name='Value')),
                ('extension', models.CharField(blank=True, max_length=64, null=True, verbose_name='Extension')),
                ('protected', models.CharField(blank=True, choices=[('', ''), ('true', 'True'), ('false', 'False')], default='', max_length=8, verbose_name='Protected')),
                ('label', models.CharField(blank=True, max_length=64, null=True, verbose_name='Label')),
                ('icon', models.CharField(blank=True, max_length=64, null=True, verbose_name='Icon')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, null=True, verbose_name='Updated')),
                ('synchronised', models.DateTimeField(blank=True, null=True, verbose_name='Synchronised')),
                ('updated_by', models.CharField(max_length=64, verbose_name='Updated by')),
                ('profile_id', models.ForeignKey(db_column='profile_id', on_delete=django.db.models.deletion.CASCADE, to='provision.devices', verbose_name='Profile')),
            ],
            options={
                'db_table': 'pbx_device_profile_keys',
            },
        ),
        migrations.CreateModel(
            name='DeviceLines',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='Key')),
                ('line_number', models.DecimalField(decimal_places=0, default=1, max_digits=3, verbose_name='Line')),
                ('server_address', models.CharField(blank=True, max_length=254, null=True, verbose_name='Server Address')),
                ('server_address_primary', models.CharField(blank=True, max_length=254, null=True, verbose_name='Primary Address')),
                ('server_address_secondary', models.CharField(blank=True, max_length=254, null=True, verbose_name='Secondary Address')),
                ('outbound_proxy_primary', models.CharField(blank=True, max_length=254, null=True, verbose_name='Primary Proxy')),
                ('outbound_proxy_secondary', models.CharField(blank=True, max_length=254, null=True, verbose_name='Secondary Proxy')),
                ('display_name', models.CharField(blank=True, max_length=254, null=True, verbose_name='Display Name')),
                ('user_id', models.CharField(blank=True, max_length=254, null=True, verbose_name='User ID')),
                ('auth_id', models.CharField(blank=True, max_length=254, null=True, verbose_name='Auth ID')),
                ('password', models.CharField(blank=True, max_length=254, null=True, verbose_name='Password')),
                ('sip_port', models.DecimalField(blank=True, decimal_places=0, default=5060, max_digits=5, null=True, verbose_name='SIP Port')),
                ('sip_transport', models.CharField(blank=True, max_length=254, null=True, verbose_name='Value')),
                ('register_expires', models.DecimalField(blank=True, decimal_places=0, default=1800, max_digits=5, null=True, verbose_name='Expires')),
                ('shared_line', models.CharField(blank=True, max_length=128, null=True, verbose_name='Shared Line')),
                ('enabled', models.CharField(blank=True, choices=[('false', 'False'), ('true', 'True')], default='true', max_length=8, verbose_name='Enabled')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, null=True, verbose_name='Updated')),
                ('synchronised', models.DateTimeField(blank=True, null=True, verbose_name='Synchronised')),
                ('updated_by', models.CharField(max_length=64, verbose_name='Updated by')),
                ('device_id', models.ForeignKey(db_column='device_id', on_delete=django.db.models.deletion.CASCADE, to='provision.devices', verbose_name='Device')),
            ],
            options={
                'db_table': 'pbx_device_lines',
            },
        ),
        migrations.CreateModel(
            name='DeviceKeys',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='Key')),
                ('category', models.CharField(blank=True, choices=[('', 'Not Set'), ('line', 'Line'), ('memory', 'Memory'), ('programmable', 'Programmable'), ('expansion-1', 'Expansion 1'), ('expansion-2', 'Expansion 2'), ('expansion-3', 'Expansion 3'), ('expansion-4', 'Expansion 4'), ('expansion-5', 'Expansion 5'), ('expansion-6', 'Expansion 6')], default='line', max_length=16, verbose_name='Category')),
                ('key_id', models.DecimalField(decimal_places=0, default=1, max_digits=11, verbose_name='Key')),
                ('key_type', models.CharField(max_length=64, verbose_name='Key type')),
                ('line', models.DecimalField(decimal_places=0, default=1, max_digits=3, verbose_name='Line')),
                ('value', models.CharField(blank=True, max_length=254, null=True, verbose_name='Value')),
                ('extension', models.CharField(blank=True, max_length=64, null=True, verbose_name='Extension')),
                ('protected', models.CharField(blank=True, choices=[('', ''), ('true', 'True'), ('false', 'False')], default='', max_length=8, verbose_name='Protected')),
                ('label', models.CharField(blank=True, max_length=64, null=True, verbose_name='Label')),
                ('icon', models.CharField(blank=True, max_length=64, null=True, verbose_name='Icon')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, null=True, verbose_name='Updated')),
                ('synchronised', models.DateTimeField(blank=True, null=True, verbose_name='Synchronised')),
                ('updated_by', models.CharField(max_length=64, verbose_name='Updated by')),
                ('device_id', models.ForeignKey(db_column='device_id', on_delete=django.db.models.deletion.CASCADE, to='provision.devices', verbose_name='Device')),
            ],
            options={
                'db_table': 'pbx_device_keys',
            },
        ),
    ]

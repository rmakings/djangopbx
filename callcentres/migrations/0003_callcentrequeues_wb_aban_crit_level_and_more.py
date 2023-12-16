# Generated by Django 4.0.4 on 2023-12-16 10:45

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('callcentres', '0002_alter_callcentreagents_unique_together'),
    ]

    operations = [
        migrations.AddField(
            model_name='callcentrequeues',
            name='wb_aban_crit_level',
            field=models.DecimalField(decimal_places=0, default=20, max_digits=3, verbose_name='Abandoned Critical Level'),
        ),
        migrations.AddField(
            model_name='callcentrequeues',
            name='wb_aban_warn_level',
            field=models.DecimalField(decimal_places=0, default=5, max_digits=3, verbose_name='Abandoned Warning Level'),
        ),
        migrations.AddField(
            model_name='callcentrequeues',
            name='wb_agents_per_row',
            field=models.DecimalField(decimal_places=0, default=6, max_digits=3, verbose_name='Number of Agents per row'),
        ),
        migrations.AddField(
            model_name='callcentrequeues',
            name='wb_show_agents',
            field=models.CharField(choices=[('false', 'False'), ('true', 'True')], default='true', max_length=8, verbose_name='Show Agents'),
        ),
        migrations.AddField(
            model_name='callcentrequeues',
            name='wb_wait_crit_level',
            field=models.DecimalField(decimal_places=0, default=20, max_digits=3, verbose_name='Waiting Critical Level'),
        ),
        migrations.AddField(
            model_name='callcentrequeues',
            name='wb_wait_warn_level',
            field=models.DecimalField(decimal_places=0, default=5, max_digits=3, verbose_name='Waiting Warning Level'),
        ),
        migrations.CreateModel(
            name='CallCentreAgentStatusLog',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='Agent Status Log')),
                ('status', models.CharField(blank=True, default='Unknown', max_length=32, null=True, verbose_name='Status')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, null=True, verbose_name='Updated')),
                ('synchronised', models.DateTimeField(blank=True, null=True, verbose_name='Synchronised')),
                ('updated_by', models.CharField(max_length=64, verbose_name='Updated by')),
                ('agent_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='callcentres.callcentreagents', verbose_name='Call Centre Agent')),
            ],
            options={
                'verbose_name_plural': 'Agent Status Log',
                'db_table': 'pbx_cc_agent_status_log',
            },
        ),
    ]
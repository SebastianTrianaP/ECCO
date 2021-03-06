# Generated by Django 2.1.7 on 2019-10-05 18:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carrito_servicio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='CarritoCompras',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numServicios', models.IntegerField()),
                ('costoTotal', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Pregunta',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('pregunta', models.TextField()),
                ('fechaPregunta', models.TextField()),
                ('respuesta', models.TextField()),
                ('fechaRespuesta', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Resena',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('texto', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.TextField()),
                ('pais', models.TextField()),
                ('ciudad', models.TextField()),
                ('idioma', models.TextField()),
                ('costo', models.FloatField()),
                ('descripcion', models.TextField()),
                ('foto', models.TextField()),
                ('numeroPersonas', models.IntegerField()),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreUsuario', models.TextField(default='', unique=True)),
                ('nombre', models.TextField()),
                ('edad', models.IntegerField()),
                ('foto', models.TextField()),
                ('descripcion', models.TextField()),
                ('telefono', models.TextField()),
                ('contrasena', models.TextField(default='1234')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
        ),
        migrations.CreateModel(
            name='Alimentacion',
            fields=[
                ('servicio_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='servicios.Servicio')),
                ('tipoComida', models.TextField()),
                ('cantidadPlatos', models.IntegerField()),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('servicios.servicio',),
        ),
        migrations.CreateModel(
            name='Alojamiento',
            fields=[
                ('servicio_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='servicios.Servicio')),
                ('tipoAlojamiento', models.TextField(choices=[('HOTEL', 'HOTEL'), ('CASA', 'CASA'), ('CAMPING', 'CAMPING'), ('MOTEL', 'MOTEL')])),
                ('numeroHabitaciones', models.IntegerField()),
                ('numeroBanos', models.IntegerField()),
                ('servicioLimpieza', models.TextField(choices=[('Si', 'Si'), ('No', 'No')])),
                ('servicioWifi', models.TextField(choices=[('Si', 'Si'), ('No', 'No')])),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('servicios.servicio',),
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('usuario_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='servicios.Usuario')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('servicios.usuario',),
        ),
        migrations.CreateModel(
            name='PaseoEcologico',
            fields=[
                ('servicio_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='servicios.Servicio')),
                ('origen', models.TextField()),
                ('destino', models.TextField(default='')),
                ('horaInicio', models.TextField()),
                ('horaFin', models.TextField()),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('servicios.servicio',),
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('usuario_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='servicios.Usuario')),
                ('paginaWeb', models.TextField()),
                ('contactoRS', models.TextField(blank=True)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('servicios.usuario',),
        ),
        migrations.CreateModel(
            name='Transporte',
            fields=[
                ('servicio_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='servicios.Servicio')),
                ('empresa', models.TextField()),
                ('tipoTransporte', models.TextField(choices=[('TERRESTRE', 'Terrestre'), ('AEREO', 'Aereo'), ('MARITIMO', 'Maritimo')])),
                ('origen', models.TextField()),
                ('destino', models.TextField()),
                ('horaSalida', models.TextField()),
                ('horaLlegada', models.TextField()),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('servicios.servicio',),
        ),
        migrations.AddField(
            model_name='usuario',
            name='polymorphic_ctype',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_servicios.usuario_set+', to='contenttypes.ContentType'),
        ),
        migrations.AddField(
            model_name='servicio',
            name='polymorphic_ctype',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_servicios.servicio_set+', to='contenttypes.ContentType'),
        ),
        migrations.AddField(
            model_name='resena',
            name='servicio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='servicios.Servicio'),
        ),
        migrations.AddField(
            model_name='pregunta',
            name='servicio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='servicios.Servicio'),
        ),
        migrations.AddField(
            model_name='carritocompras',
            name='servicios',
            field=models.ManyToManyField(to='servicios.Servicio'),
        ),
        migrations.AddField(
            model_name='carrito_servicio',
            name='carrito',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='servicios.CarritoCompras'),
        ),
        migrations.AddField(
            model_name='carrito_servicio',
            name='servicio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='servicios.Servicio'),
        ),
        migrations.AddField(
            model_name='servicio',
            name='proveedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='servicios.Proveedor'),
        ),
        migrations.AddField(
            model_name='resena',
            name='cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='servicios.Cliente'),
        ),
        migrations.AddField(
            model_name='pregunta',
            name='cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='servicios.Cliente'),
        ),
        migrations.AddField(
            model_name='carritocompras',
            name='cliente',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='servicios.Cliente'),
        ),
    ]

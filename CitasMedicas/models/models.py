from odoo import models, fields

class CitaMedica(models.Model):
    _name = 'medical.appointment'
    _description = 'Cita Médica'

    patient_id = fields.Many2one('medical.patient', string="Paciente", required=True)
    doctor_id = fields.Many2one('medical.doctor', string="Médico", required=True)
    appointment_date = fields.Date(string="Fecha de la Cita", required=True)
    appointment_time = fields.Float(string="Hora de la Cita", required=True)
    notes = fields.Text(string="Notas")

class PacienteMedico(models.Model):
    _name = 'medical.patient'
    _description = 'Paciente Médico'

    name = fields.Char(string="Nombre", required=True)
    dob = fields.Date(string="Fecha de Nacimiento")
    phone = fields.Char(string="Teléfono")
    email = fields.Char(string="Correo Electrónico")

class Medico(models.Model):
    _name = 'medical.doctor'
    _description = 'Médico'

    name = fields.Char(string="Nombre", required=True)
    specialty = fields.Char(string="Especialidad")
    phone = fields.Char(string="Teléfono")
    email = fields.Char(string="Correo Electrónico")
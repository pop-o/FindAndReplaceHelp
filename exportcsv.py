import csv
from django.core.management.base import BaseCommand
from django.utils import timezone
from myapp.models import ParkingDetails  # Replace 'myapp' with your app name

class Command(BaseCommand):
    help = 'Export ParkingDetails table to a CSV file compatible with UploadParkingDetailsAPIView'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='Path to save the CSV file')

    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']
        self.stdout.write(f"Exporting ParkingDetails to {file_path}")

        # Define the CSV headers
        headers = [
            'receipt_id',
            'vehicle_number',
            'vehicle_type',
            'checkin_time',
            'checkout_time',
            'amount',
            'total_time',
            'bill_no',
            'checkedin_by',
            'checkedout_by',
        ]

        # Open the CSV file for writing
        with open(file_path, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=headers)
            writer.writeheader()

            # Fetch all ParkingDetails records
            parking_details = ParkingDetails.objects.all()

            for record in parking_details:
                # Format checkin_time and checkout_time to match the expected format
                checkin_time = record.checkin_time.strftime('%Y-%m-%d %H:%M:%S') if record.checkin_time else 'null'
                checkout_time = record.checkout_time.strftime('%Y-%m-%d %H:%M:%S') if record.checkout_time else 'null'

                # Handle nullable fields
                vehicle_number = record.vehicle_number if record.vehicle_number else 'null'
                vehicle_type = record.vehicle_type if record.vehicle_type else 'null'
                amount = str(record.amount) if record.amount is not None else 'null'
                total_time = str(record.total_time) if record.total_time else 'null'
                bill_no = str(record.bill_no) if record.bill_no is not None else 'null'
                checkedin_by = str(record.checkedin_by.id) if record.checkedin_by else 'null'
                checkedout_by = str(record.checkedout_by.id) if record.checkedout_by else 'null'

                # Write the row to the CSV
                writer.writerow({
                    'receipt_id': record.receipt_id,
                    'vehicle_number': vehicle_number,
                    'vehicle_type': vehicle_type,
                    'checkin_time': checkin_time,
                    'checkout_time': checkout_time,
                    'amount': amount,
                    'total_time': total_time,
                    'bill_no': bill_no,
                    'checkedin_by': checkedin_by,
                    'checkedout_by': checkedout_by,
                })

        self.stdout.write(self.style.SUCCESS(f"Successfully exported ParkingDetails to {file_path}"))

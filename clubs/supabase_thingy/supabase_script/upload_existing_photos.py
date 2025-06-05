import os
from django.core.management.base import BaseCommand
from supabase import create_client
from django.conf import settings
from storage3.exceptions import StorageApiError

class Command(BaseCommand):
    help = "Recursively upload existing images from media/photos/ and all subfolders to Supabase Storage"

    def handle(self, *args, **kwargs):
        SUPABASE_URL = os.getenv("SUPABASE_URL")
        SUPABASE_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImZjbmR3aHFsc2djZ3VpZmhndnR6Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDI4Mjk3MTksImV4cCI6MjA1ODQwNTcxOX0.yOZny9VBLW3b2W8SqYs4ryYMqQEZdhL70U_9y0V31W4'
        supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

        media_folder = os.path.join(settings.MEDIA_ROOT, "photos")

        if not os.path.exists(media_folder):
            self.stdout.write(self.style.ERROR(f"❌ Media folder {media_folder} does not exist."))
            return

        # Walk through all subdirectories and upload files
        for root, _, files in os.walk(media_folder):
            for filename in files:
                file_path = os.path.join(root, filename)  # Full local file path

                if os.path.isfile(file_path):  # Ensure it's a file
                    # Get the relative path inside `photos/` to maintain subfolder structure
                    relative_path = os.path.relpath(file_path, media_folder)  # e.g., "2024/12/12/image.jpg"
                    supabase_path = f"photos/{relative_path}".replace("\\", "/")  # ✅ Fix Windows backslashes

                    print(f"📤 Checking if {supabase_path} exists in Supabase...")

                    # **Step 1: Check if file exists in Supabase**
                    existing_files = supabase.storage.from_("meedia").list("photos/")
                    existing_paths = [file["name"] for file in existing_files]

                    if supabase_path in existing_paths:
                        print(f"🔄 File {supabase_path} already exists. Deleting before re-uploading.")
                        supabase.storage.from_("meedia").remove([supabase_path])

                    # **Step 2: Upload File to Supabase**
                    print(f"📤 Uploading {relative_path} to Supabase as {supabase_path}...")

                    with open(file_path, "rb") as file:
                        try:
                            response = supabase.storage.from_("meedia").upload(
                                supabase_path, file, file_options={"content-type": "image/jpeg"}
                            )
                            if response and hasattr(response, "error") and response.error:
                                self.stdout.write(self.style.ERROR(f"❌ Upload failed for {relative_path}: {response.error}"))
                            else:
                                self.stdout.write(self.style.SUCCESS(f"✅ Uploaded {relative_path} successfully!"))
                        except StorageApiError as e:
                            self.stdout.write(self.style.ERROR(f"⚠️ Upload error for {relative_path}: {e}"))

        self.stdout.write(self.style.SUCCESS("🎉 All images from media/photos/ and subfolders uploaded to Supabase!"))
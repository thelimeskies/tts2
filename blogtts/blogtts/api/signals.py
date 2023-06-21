# # Signals to create audio from blog posts

# from blogtts.api.tasks import content_to_audio


# def create_audio(sender, instance, created, **kwargs):
#     if created:
#         content_to_audio.delay(instance.pk)

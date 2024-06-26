# Appraise Evaluation System



Generating an example campaign with direct assessment tasks with SQM quality
levels. Note it uses exact same batches as standard direct assessment tasks:

    python manage.py StartNewCampaign Examples/DirectSQM_Spanish/manifest.json --batches-json Examples/DirectSQM_Spanish/annotator_consisteny_check_Spanish.json  --csv-output Examples/DirectSQM_Spanish/output.csv

    # See Examples/DirectSQM/outputs.csv for a SSO login for the annotator account
    # Collect some annotations, then export annotation scores...

    python manage.py ExportSystemScoresToCSV spasqm1

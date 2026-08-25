from client import ViralVideoHookDetectorAutoClipCuratorClient

def main():
    client = ViralVideoHookDetectorAutoClipCuratorClient()
    res = client.curate_viral_short_clips('https://assets.genpark.ai/video/founders_talk_show.mp4', 3)
    print('Curation Job: ' + res['curation_job_id'] + ' (' + str(res['viral_clips_curated_count']) + ' clips)')
    print('Top Virality Score: ' + str(res['highest_virality_score_pct']) + '% | Vertical 9:16: ' + str(res['auto_speaker_reframe_vertical_9_16']))
    print('Burned Captions: ' + str(res['karaoke_style_animated_captions_burned']) + ' (B-Roll: ' + str(res['b_roll_visual_inserts_count']) + ')')
    for u in res['rendered_shorts_urls']:
        print('  - ' + u)

if __name__ == '__main__':
    main()

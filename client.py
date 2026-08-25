class ViralVideoHookDetectorAutoClipCuratorClient:
    def curate_viral_short_clips(self, source_podcast_video_url='https://assets.genpark.ai/video/tech_podcast_ep42.mp4', target_clips_count=3):
        return {
            'curation_job_id': 'ops_clp_5519',
            'source_video': source_podcast_video_url,
            'viral_clips_curated_count': target_clips_count,
            'highest_virality_score_pct': 98.6,
            'auto_speaker_reframe_vertical_9_16': True,
            'karaoke_style_animated_captions_burned': True,
            'b_roll_visual_inserts_count': 6,
            'rendered_shorts_urls': [
                'https://assets.genpark.ai/shorts/hook_1_secret_of_agi.mp4',
                'https://assets.genpark.ai/shorts/hook_2_billion_dollar_startup.mp4'
            ]
        }

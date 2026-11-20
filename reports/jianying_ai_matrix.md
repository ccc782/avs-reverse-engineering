# 剪映 AI 能力矩阵（证据化）

- 扫描对象：`11.7.0.14652` 的 `Resources\models` 与 `Resources\*`
- 端侧模型包：**45** 个，合计 **213 MB**
- RTTI 类名：**15041**（全量在 `rtti_jy_veditor.md`）
- 可从外部触发的 AI 命令：60 条
- 云端端点样本：195 条

| 能力 | 落点 | 端侧模型包（MB / 文件） | 类级线索 | 可触发命令 | 云端端点 |
| --- | --- | --- | ---: | --- | --- |
| 人像抠像/视频分割 | 端侧 | `hairparser` 0.1MB/1f<br>`headsegmodel` 0.0MB/1f<br>`humanparsingmodel` 0.7MB/1f<br>`mattingmodel` 20.0MB/7f | 59 个<br>`lvve::AIMattingClient`<br>`lvve::AIMattingClientPubApi`<br>`lvve::AiMattingApplyParams` | `video.setMatting`<br>`video.clearMatting`<br>`video.applyAllChroma` | — |
| 绿幕/色度键 | 端侧 | — | 42 个<br>`lvve::ChromaColorParam`<br>`lvve::ChromaEdgeSmoothParam`<br>`lvve::ChromaIntensityParam` | `video.setChromaColor`<br>`video.setChromaIntensity`<br>`video.setChromaShadow`<br>`video.setChromaEdgeSmooth` | — |
| 美颜/美妆/塑形 | 端侧 | `bingo_facegan_model` 5.1MB/1f<br>`facebeautifymodel` 0.5MB/1f<br>`facefitting` 1.2MB/2f<br>`petfacemodel` 1.0MB/1f | 74 个<br>`lvve::BeautyBodyAutoPreset`<br>`lvve::BeautyBodyPreset`<br>`lvve::BeautyFaceAutoPreset` | `video.setFigure`<br>`video.setMakeupRoot`<br>`video.clearFigure`<br>`video.setFigureFaceId` | — |
| 人脸识别/聚类/验证 | 端侧 | `faceclustingmodel` 4.7MB/2f<br>`faceverifymodel` 4.1MB/1f<br>`freidmodel` 23.6MB/3f | 0 个 | — | — |
| 手部/骨骼/动作 | 双路 | `avatar3d` 10.0MB/1f<br>`avatar_drive` 0.6MB/1f<br>`handmodel` 0.6MB/3f<br>`skeleton_model` 0.4MB/1f | 113 个<br>`Concurrency::details::_TaskProcHandle`<br>`lvve::AttachmentVipHandwrite`<br>`lvve::KeyframeHandwrite` | `video.addDigitalHuman`<br>`video.updateDigitalHuman` | `https://lv-api-sinfonlinec.ulikecam.com/lv/edit/digital_huma` |
| 深度/显著性/场景 | 端侧 | `alg_scene_normal` 5.1MB/1f<br>`colorcard` 0.2MB/1f<br>`depthmodel` 1.2MB/1f<br>`scene_normal_model` 5.1MB/1f | 0 个 | — | — |
| 插帧/超分/去闪烁 | 端侧 | `deflicker` 0.1MB/1f<br>`interpolation` 10.0MB/1f<br>`umvfi` 0.1MB/1f | 31 个<br>`lvve::Deflicker`<br>`lvve::SuperResolution`<br>`lvve::SuperResolutionParam` | `video.setStable`<br>`video.setVideoAlgorithm` | — |
| 防抖/稳定 | 端侧 | — | 18 个<br>`lvve::GameplayAdjustableConfig`<br>`lvve::NodeWrapperStableMatrixPath`<br>`lvve::SmartStableResult` | `video.setStable` | — |
| 降噪（画/音） | 端侧 | `audiomodel` 31.1MB/8f<br>`noise_reduction` 0.2MB/1f | 23 个<br>`lvve::AudioRealtimeDenoiseParam`<br>`lvve::MaterialRealtimeDenoise`<br>`lvve::NoiseReduction` | `video.denoiseOn`<br>`video.denoiseOff`<br>`audio.denoiseOn`<br>`audio.denoiseOff` | — |
| 人声分离/修音/变声 | 端侧 | `audiomodel` 31.1MB/8f | 43 个<br>`lvve::AttachmentArticleVideoToneConfig`<br>`lvve::AttachmentMidvideoToneInfo`<br>`lvve::AttachmentOneoffDraft` | `video.pitchOn`<br>`video.pitchOff`<br>`audio.pitchOn`<br>`audio.pitchOff` | — |
| 语音识别/字幕/歌词 | 双路 | `audiomodel` 31.1MB/8f | 197 个<br>`lvve::AddLyricEffectParam`<br>`lvve::AiMusicLyric`<br>`lvve::AttachmentAIClipperTranscriptControl` | `text.addSubtitles`<br>`text.deleteTextToAudioIds`<br>`text.updateSubtitleTemplate`<br>`text.setSubtitleKeywords` | `/lv/v1/audio_subtitle/feedback`<br>`/lv/v1/audio_subtitle/get_keyword`<br>`/lv/v1/audio_subtitle/highlight` |
| TTS/配音/音色克隆 | 云侧 | — | 21 个<br>`lvve::DigitalHumanTtsMeta`<br>`lvve::TtsBenefitInfo`<br>`lvve::TtsBenefitInfoParam` | `text.deleteTextToAudioIds` | `/lv/v1/text_to_audio`<br>`/lv/v1/voice/delete_voice_clone`<br>`/lv/v1/voice/release_voice_clone` |
| 视觉跟踪/物体锁定 | 端侧 | `object_tracking` 0.2MB/1f | 84 个<br>`lvve::AddObjectLockedParam`<br>`lvve::AttachmentEditableMaterialTracking`<br>`lvve::IObjectLockAlgorithm` | `video.addObjectLocked`<br>`video.updateObjectLocked`<br>`video.removeObjectLocked`<br>`text.addVideoTracker` | — |
| 智能裁剪/运镜/构图 | 端侧 | `saliency_seg_model` 3.7MB/1f | 24 个<br>`lvve::MaterialSmartCrop`<br>`lvve::NodeWrapperSegmentVideoSmartCropVersion`<br>`lvve::SmartCropManager` | `video.removeSmartCrop`<br>`video.addSmartCrop`<br>`video.setSmartColorAdjust` | — |
| 智能打光/眼神/画质修复 | 端侧 | `bingo_facegan_model` 5.1MB/1f<br>`idream` 0.9MB/1f | 74 个<br>`lvve::AttachmentAutoEnhancementConfig`<br>`lvve::AttachmentAutoEnhancementControl`<br>`lvve::AttachmentAutoEnhancementSingleConfig` | `video.setVideoAlgorithm` | — |
| 素材语义检索 | 双路 | `media_search` 31.6MB/8f<br>`SegmentJS` 1.3MB/4f | 0 个 | — | `/lv/v1/cloud_property/search`<br>`/lv/v1/effect/search`<br>`/lv/v1/pc/search/commercial_templates` |
| AIGC 生成（文/图/视频） | 双路 | `idream` 0.9MB/1f<br>`jianying_aigc_charge` 0.0MB/1f<br>`mangamodel` 2.9MB/1f | 128 个<br>`lvve::AigcAudioGenerateInfo`<br>`lvve::AigcAudioGenerateInfoParam`<br>`lvve::AigcGenerate` | `attachment.setAiCreatorContent`<br>`attachment.updateAiCreation`<br>`attachment.updateAiReelAgent` | `/lv/v1/aigc_text/get_voiceclone_text`<br>`/lv/v1/asset/create_cloud_asset`<br>`/lv/v1/coordination/cluster_create` |
| 数字人 | 双路 | `avatar3d` 10.0MB/1f<br>`avatar_drive` 0.6MB/1f | 47 个<br>`lvve::AttachmentDigitalHumanTemplateToVideoInfo`<br>`lvve::DigitalHumanAudioMeta`<br>`lvve::DigitalHumanBackground` | `video.addDigitalHuman`<br>`video.updateDigitalHuman`<br>`video.updateDigitalHumanRendered` | `https://lv-api-sinfonlinec.ulikecam.com/lv/edit/digital_huma` |
| 场景检测/镜头切分 | 云侧 | — | 7 个<br>`lvve::AttachmentMidVideoHighlight`<br>`lvve::HighlightCutResult`<br>`lyra::CancelVideoHighlightcutProcessRespStruct` | — | `/lv/v1/audio_subtitle/highlight`<br>`/lv/v1/music_scene_check`<br>`https://lv-api.ulikecam.com/lv/v1/audio_subtitle/highlight` |
| 隐形水印/AI 标识 | 双路 | `invisible_watermark` 1.5MB/2f | 60 个<br>`lvve::AttachmentWatermarkInfo`<br>`lvve::AttachmentWatermarkInfoControl`<br>`lyra::AddAudioWatermarkRespStruct` | `draft.updateDraftAIGCWatermark` | `/lv/v1/watermark/get_watermark` |

## 端侧模型包全表

共 45 个目录，合计 213 MB。

| 目录 | MB | 文件数 |
| --- | ---: | ---: |
| `media_search` | 31.6 | 8 |
| `audiomodel` | 31.1 | 8 |
| `freidmodel` | 23.6 | 3 |
| `tt_mobilevos` | 22.3 | 2 |
| `mattingmodel` | 20.0 | 7 |
| `tt_interactive_matting` | 10.5 | 1 |
| `avatar3d` | 10.0 | 1 |
| `interpolation` | 10.0 | 1 |
| `alg_scene_normal` | 5.1 | 1 |
| `bingo_facegan_model` | 5.1 | 1 |
| `scene_normal_model` | 5.1 | 1 |
| `faceclustingmodel` | 4.7 | 2 |
| `tt_gendergan` | 4.3 | 1 |
| `faceverifymodel` | 4.1 | 1 |
| `saliency_seg_model` | 3.7 | 1 |
| `mangamodel` | 2.9 | 1 |
| `tt_facefitting_3d` | 2.0 | 1 |
| `v2-models` | 1.7 | 12 |
| `invisible_watermark` | 1.5 | 2 |
| `tt_salient_human` | 1.4 | 1 |
| `SegmentJS` | 1.3 | 4 |
| `depthmodel` | 1.2 | 1 |
| `facefitting` | 1.2 | 2 |
| `aec` | 1.1 | 2 |
| `petfacemodel` | 1.0 | 1 |
| `v1-models` | 1.0 | 8 |
| `idream` | 0.9 | 1 |
| `humanparsingmodel` | 0.7 | 1 |
| `avatar_drive` | 0.6 | 1 |
| `handmodel` | 0.6 | 3 |
| `skin_seg` | 0.6 | 2 |
| `facebeautifymodel` | 0.5 | 1 |
| `nh_nodehub_image` | 0.4 | 1 |
| `skeleton_model` | 0.4 | 1 |
| `colorcard` | 0.2 | 1 |
| `noise_reduction` | 0.2 | 1 |
| `object_tracking` | 0.2 | 1 |
| `deflicker` | 0.1 | 1 |
| `hairparser` | 0.1 | 1 |
| `tt_eyefitting` | 0.1 | 1 |
| `umvfi` | 0.1 | 1 |
| `headsegmodel` | 0.0 | 1 |
| `jianying_aigc_charge` | 0.0 | 1 |
| `nh_script` | 0.0 | 1 |
| `oilpaintbrush` | 0.0 | 1 |

## 云端端点（去重样本）

```
/lv/v1/account/get_pippit_token
/lv/v1/account/get_pippit_user_info
/lv/v1/account/user
/lv/v1/ai_writing/get_results_by_images
/lv/v1/ai_writing/get_results_by_texts
/lv/v1/aigc_text/get_voiceclone_text
/lv/v1/asset/create_cloud_asset
/lv/v1/asset/detail
/lv/v1/asset/prepare_upload_cloud
/lv/v1/audio_subtitle/feedback
/lv/v1/audio_subtitle/get_keyword
/lv/v1/audio_subtitle/highlight
/lv/v1/audio_subtitle/query
/lv/v1/audio_subtitle/submit
/lv/v1/audio_subtitle/update_keyword
/lv/v1/benefit_redemption
/lv/v1/calc_video_score
/lv/v1/capflow/cancel
/lv/v1/capflow/history_task
/lv/v1/capflow/query
/lv/v1/capflow/submit
/lv/v1/check_rate_limit
/lv/v1/check_spam
/lv/v1/cloud/auto_upload/get_setting
/lv/v1/cloud/auto_upload/update_setting
/lv/v1/cloud/group/free_space_gifted
/lv/v1/cloud/group/get_experiment
/lv/v1/cloud/group/give_temp_quota
/lv/v1/cloud/upload/get_record
/lv/v1/cloud_property/get_user_recent_package
/lv/v1/cloud_property/property_count
/lv/v1/cloud_property/search
/lv/v1/common_task/cancel
/lv/v1/common_task/new
/lv/v1/common_task/query
/lv/v1/common_task/sync
/lv/v1/coordination/batch_send_message
/lv/v1/coordination/check_white_list
/lv/v1/coordination/cluster_create
/lv/v1/coordination/get_share_info
/lv/v1/coordination/mark_notice/list_draft
/lv/v1/coordination/mark_notice/read_draft
/lv/v1/coordination/owner_share_list
/lv/v1/coordination/record_delete
/lv/v1/coordination/share_create
/lv/v1/coordination/share_update
/lv/v1/coordination/shared_record_list
/lv/v1/copilot/conversation/history
/lv/v1/copilot/get_preupload_time
/lv/v1/copilot/modify_message
/lv/v1/copilot/section/history
/lv/v1/copilot/upload_material
/lv/v1/custom_service/get_entrance
/lv/v1/custom_service/get_entrance_allow_guest
/lv/v1/custom_service/im/post_context_info
/lv/v1/edit/get_config
/lv/v1/effect/search
/lv/v1/encrypt/get_public_key
/lv/v1/ever_photo/get_token
/lv/v1/ever_photo/promote_asset
/lv/v1/font/check
/lv/v1/get_collection_songs
/lv/v1/get_collections
/lv/v1/get_music_effect_collections
/lv/v1/get_my_douyin_songs
/lv/v1/get_my_tiktok_songs
/lv/v1/get_recommend_songs
/lv/v1/get_sami_token
/lv/v1/get_user_vid_list
/lv/v1/group/templates
/lv/v1/image/anime_copyright_checker
/lv/v1/image/content_classifier
/lv/v1/image/face_compare
/lv/v1/intelligent_edit/security_audit
/lv/v1/lan_transfer/get_user_devices_info
/lv/v1/lan_transfer/upload_device_info
/lv/v1/multi_get_songs
/lv/v1/music/filter
/lv/v1/music/get_recommend_music
/lv/v1/music/similar_music_rec
/lv/v1/music/template_music_recommend
/lv/v1/music_finger
/lv/v1/music_scene_check
/lv/v1/oauth/access_token
/lv/v1/pc/aweme_collection_songs
/lv/v1/pc/commerce_replicate/operation_collection
/lv/v1/pc/commerce_replicate/operation_collection_contents
/lv/v1/pc/export_page/share_douyin_sign
/lv/v1/pc/export_page/share_douyin_vid
/lv/v1/pc/export_page/share_xigua
/lv/v1/pc/get_user_info
/lv/v1/pc/get_user_keyboard_shortcut
/lv/v1/pc/homepage/templates
/lv/v1/pc/replicate/delete
/lv/v1/pc/replicate/get_collection_templates
/lv/v1/pc/replicate/multi_get_templates
/lv/v1/pc/search/commercial_templates
/lv/v1/pc/search/sug
/lv/v1/pc/search/templates
/lv/v1/pc/share/exchange_rights
/lv/v1/pc/share/get_user_rights
/lv/v1/pc/share/is_activity_valid
/lv/v1/pc/share/token_gen
/lv/v1/pc/storyboard/entrance_click
/lv/v1/pc/to_shoot/add_item
/lv/v1/pc/to_shoot/get_list
/lv/v1/pc/to_shoot/remove_item
/lv/v1/pc/update_user_keyboard_shortcut
/lv/v1/pc/zenith/cancel_task
/lv/v1/pc/zenith/fetch_result
/lv/v1/pc/zenith/query_task
/lv/v1/pc/zenith/submit_task
/lv/v1/persona/get_features
/lv/v1/personal/pc/templates
/lv/v1/purchase/purchase_templates
/lv/v1/replicate/add
/lv/v1/replicate/add_usage_amount
/lv/v1/replicate/delete
/lv/v1/replicate/get_collections
/lv/v1/replicate/update_settings
```
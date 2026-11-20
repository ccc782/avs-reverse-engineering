# 剪映 AI 深挖：接口 / 流水线 / 模型规格 / 云 API

- AI 命中的 RTTI 类名：**1304**
- 反推出的 AI RPC：**567**（按域分布：AIGC 生成 106，跟踪/锁定 100，音频 AI 68，画质 58，智能剪辑决策 52，AI 任务调度 44，字幕/文本 44，抠像/分割 36，美颜/塑形 36，人脸 21，其它 2）
- AI 流水线目录：**40**
- 端侧模型包：**45**（合计 214 MB）
- 云 API 服务：**139**

## 一、AI RPC 全表（从 Req/Resp 结构体反推）

| 域 | 命名空间 | 方法 | 请求结构 | 响应结构 |
| --- | --- | --- | --- | --- |
| AI 任务调度 | `lyra` | `AppendAsyncTaskListener` | — | `lyra::AppendAsyncTaskListenerRespStruct` |
| AI 任务调度 | `lyra` | `CancelAsyncTask` | — | `lyra::CancelAsyncTaskRespStruct` |
| AI 任务调度 | `lyra` | `CancelAsyncTasks` | `lyra::CancelAsyncTasksReqStruct` | `lyra::CancelAsyncTasksRespStruct` |
| AI 任务调度 | `lyra` | `CancelDraftAsyncTasks` | — | `lyra::CancelDraftAsyncTasksRespStruct` |
| AI 任务调度 | `lyra` | `CancelVideoFramesAsync` | — | `lyra::CancelVideoFramesAsyncRespStruct` |
| AI 任务调度 | `lyra` | `CreateAsyncTaskWithPrepare` | — | `lyra::CreateAsyncTaskWithPrepareRespStruct` |
| AI 任务调度 | `lyra` | `CreateAsyncTasks` | `lyra::CreateAsyncTasksReqStruct` | `lyra::CreateAsyncTasksRespStruct` |
| AI 任务调度 | `lyra` | `CreateAsyncTasksWithCallback` | `lyra::CreateAsyncTasksWithCallbackReqStruct` | `lyra::CreateAsyncTasksWithCallbackRespStruct` |
| AI 任务调度 | `lyra` | `CreateBatchAsyncTasksWithPrepare` | — | `lyra::CreateBatchAsyncTasksWithPrepareRespStruct` |
| AI 任务调度 | `lyra` | `GetAsyncTask` | `lyra::GetAsyncTaskReqStruct` | `lyra::GetAsyncTaskRespStruct` |
| AI 任务调度 | `lyra` | `GetAsyncTaskPersistDir` | — | `lyra::GetAsyncTaskPersistDirRespStruct` |
| AI 任务调度 | `lyra` | `GetAsyncTaskPostRealProgressEnable` | — | `lyra::GetAsyncTaskPostRealProgressEnableRespStruct` |
| AI 任务调度 | `lyra` | `GetAsyncTasks` | `lyra::GetAsyncTasksReqStruct` | `lyra::GetAsyncTasksRespStruct` |
| AI 任务调度 | `lyra` | `GetDigitalHumanBoundingBoxPositionAsync` | — | `lyra::GetDigitalHumanBoundingBoxPositionAsyncRespStruct` |
| AI 任务调度 | `lyra` | `GetGpuInfoAsync` | — | `lyra::GetGpuInfoAsyncRespStruct` |
| AI 任务调度 | `lyra` | `GetMainSeqAsync` | — | `lyra::GetMainSeqAsyncRespStruct` |
| AI 任务调度 | `lyra` | `GetSegmentProgress` | — | `lyra::GetSegmentProgressRespStruct` |
| AI 任务调度 | `lyra` | `GetShadowEditorGpuInfoAsync` | — | `lyra::GetShadowEditorGpuInfoAsyncRespStruct` |
| AI 任务调度 | `lyra` | `GetStickerBoundingBoxPositionAsync` | — | `lyra::GetStickerBoundingBoxPositionAsyncRespStruct` |
| AI 任务调度 | `lyra` | `GetTotalProgress` | — | `lyra::GetTotalProgressRespStruct` |
| AI 任务调度 | `lyra` | `GetVideoFramesAsync` | `lyra::GetVideoFramesAsyncReqStruct` | `lyra::GetVideoFramesAsyncRespStruct` |
| AI 任务调度 | `lyra` | `GetVideoImageAsync` | — | `lyra::GetVideoImageAsyncRespStruct` |
| AI 任务调度 | `lyra` | `GetVideoImageRealAsync` | — | `lyra::GetVideoImageRealAsyncRespStruct` |
| AI 任务调度 | `lyra` | `GetVideoTimeOriginImageAsync` | — | `lyra::GetVideoTimeOriginImageAsyncRespStruct` |
| AI 任务调度 | `lyra` | `GetVideoUiImageAsync` | — | `lyra::GetVideoUiImageAsyncRespStruct` |
| AI 任务调度 | `lyra` | `GetWatermarkBoundingBoxRectAndPositionAsync` | — | `lyra::GetWatermarkBoundingBoxRectAndPositionAsyncRespStruct` |
| AI 任务调度 | `lyra` | `GetWatermarkBoundingBoxRectAsync` | — | `lyra::GetWatermarkBoundingBoxRectAsyncRespStruct` |
| AI 任务调度 | `lyra` | `InitAsyncTaskManager` | — | `lyra::InitAsyncTaskManagerRespStruct` |
| AI 任务调度 | `lyra` | `LoadAttachmentsAsync` | — | `lyra::LoadAttachmentsAsyncRespStruct` |
| AI 任务调度 | `lyra` | `PreCreateAsyncTasks` | `lyra::PreCreateAsyncTasksReqStruct` | `lyra::PreCreateAsyncTasksRespStruct` |
| AI 任务调度 | `lyra` | `RegisterAlgorithmCacheProgressCallback` | — | `lyra::RegisterAlgorithmCacheProgressCallbackRespStruct` |
| AI 任务调度 | `lyra` | `RegisterPlayProgressCallback` | — | `lyra::RegisterPlayProgressCallbackRespStruct` |
| AI 任务调度 | `lyra` | `RegisterPlayerProgress` | — | `lyra::RegisterPlayerProgressRespStruct` |
| AI 任务调度 | `lyra` | `RetryAlgorithmBatchAsyncTasks` | — | `lyra::RetryAlgorithmBatchAsyncTasksRespStruct` |
| AI 任务调度 | `lyra` | `SetConsumeProgressCallback` | — | `lyra::SetConsumeProgressCallbackRespStruct` |
| AI 任务调度 | `lyra` | `SetOnBindTasksProgressCallback` | — | `lyra::SetOnBindTasksProgressCallbackRespStruct` |
| AI 任务调度 | `lyra` | `SetOnBindTasksTypeProgressCallback` | — | `lyra::SetOnBindTasksTypeProgressCallbackRespStruct` |
| AI 任务调度 | `lyra` | `SetOnTasksProgressCallback` | — | `lyra::SetOnTasksProgressCallbackRespStruct` |
| AI 任务调度 | `lyra` | `SetupAlgorithmCacheTaskAsync` | — | `lyra::SetupAlgorithmCacheTaskAsyncRespStruct` |
| AI 任务调度 | `lyra` | `SetupAsyncTaskPipelineListener` | — | `lyra::SetupAsyncTaskPipelineListenerRespStruct` |
| AI 任务调度 | `lyra` | `SingleResourcePlayerRegisterPlayerProgress` | — | `lyra::SingleResourcePlayerRegisterPlayerProgressRespStruct` |
| AI 任务调度 | `lyra` | `UnregisterAlgorithmCacheProgressCallback` | — | `lyra::UnregisterAlgorithmCacheProgressCallbackRespStruct` |
| AI 任务调度 | `lyra` | `UpdateTaskProgressManually` | — | `lyra::UpdateTaskProgressManuallyRespStruct` |
| AI 任务调度 | `lyra` | `UpdateTaskProgressProportionManually` | — | `lyra::UpdateTaskProgressProportionManuallyRespStruct` |
| AIGC 生成 | `lyra` | `AIGCEffectStartVETaskMixNode` | `lyra::AIGCEffectStartVETaskMixNodeReq` | `lyra::AIGCEffectStartVETaskMixNodeResp` |
| AIGC 生成 | `lyra` | `AIGCEffectStartVETaskMixNodeConvert` | — | `lyra::AIGCEffectStartVETaskMixNodeConvertResp` |
| AIGC 生成 | `lyra` | `AddAICreateEditedEditor` | — | `lyra::AddAICreateEditedEditorRespStruct` |
| AIGC 生成 | `lyra` | `AddAigcGenerate` | — | `lyra::AddAigcGenerateRespStruct` |
| AIGC 生成 | `lyra` | `AddAigcGenerateItems` | — | `lyra::AddAigcGenerateItemsRespStruct` |
| AIGC 生成 | `lyra` | `AddAigcSegment` | — | `lyra::AddAigcSegmentRespStruct` |
| AIGC 生成 | `lyra` | `AddArticleVideoShotGeneratedRecord` | `lyra::AddArticleVideoShotGeneratedRecordReqStruct` | `lyra::AddArticleVideoShotGeneratedRecordRespStruct` |
| AIGC 生成 | `lyra` | `AddHistoryChangeCallback` | `lyra::AddHistoryChangeCallbackReqStruct` | `lyra::AddHistoryChangeCallbackRespStruct` |
| AIGC 生成 | `lyra` | `AddWorkflowGenerateNode` | — | `lyra::AddWorkflowGenerateNodeRespStruct` |
| AIGC 生成 | `lyra` | `AigcWatermarkStatusCallback` | — | `lyra::AigcWatermarkStatusCallbackRespStruct` |
| AIGC 生成 | `lyra` | `ApplyAiGenerateImageWriteBack` | — | `lyra::ApplyAiGenerateImageWriteBackRespStruct` |
| AIGC 生成 | `lyra` | `ApplyAiGenerateVideoWriteBack` | — | `lyra::ApplyAiGenerateVideoWriteBackRespStruct` |
| AIGC 生成 | `lyra` | `ApplyAigcGenerateAttachment` | — | `lyra::ApplyAigcGenerateAttachmentRespStruct` |
| AIGC 生成 | `lyra` | `ApplyAigcGenerateAudio` | — | `lyra::ApplyAigcGenerateAudioRespStruct` |
| AIGC 生成 | `lyra` | `ApplyScriptAiCutClipInfoToMainDraft` | — | `lyra::ApplyScriptAiCutClipInfoToMainDraftRespStruct` |
| AIGC 生成 | `lyra` | `AutoSortAndReplaceArticleVideoAllVideos` | `lyra::AutoSortAndReplaceArticleVideoAllVideosReqStruct` | `lyra::AutoSortAndReplaceArticleVideoAllVideosRespStruct` |
| AIGC 生成 | `lyra` | `BatchAddAigcSegments` | — | `lyra::BatchAddAigcSegmentsRespStruct` |
| AIGC 生成 | `lyra` | `CancelAIGCTask` | `lyra::CancelAIGCTaskReqStruct` | `lyra::CancelAIGCTaskRespStruct` |
| AIGC 生成 | `lyra` | `CheckAllAIGCContent` | — | `lyra::CheckAllAIGCContentRespStruct` |
| AIGC 生成 | `lyra` | `CheckUseAIGCContent` | `lyra::CheckUseAIGCContentReqStruct` | `lyra::CheckUseAIGCContentRespStruct` |
| AIGC 生成 | `lyra` | `ClearVideoAigcAlgorithmState` | — | `lyra::ClearVideoAigcAlgorithmStateRespStruct` |
| AIGC 生成 | `lyra` | `ConvertDraftToArticleVideoDraft` | — | `lyra::ConvertDraftToArticleVideoDraftRespStruct` |
| AIGC 生成 | `lyra` | `ConvertFromArticleVideoDraft` | — | `lyra::ConvertFromArticleVideoDraftRespStruct` |
| AIGC 生成 | `lyra` | `ConvertFromArticleVideoDraftToJson` | — | `lyra::ConvertFromArticleVideoDraftToJsonRespStruct` |
| AIGC 生成 | `lyra` | `DestoryLockObjectAlgorithm` | — | `lyra::DestoryLockObjectAlgorithmRespStruct` |
| AIGC 生成 | `lyra` | `DestorySegmentPrerender` | — | `lyra::DestorySegmentPrerenderRespStruct` |
| AIGC 生成 | `lyra` | `EditScriptRegenerate` | `lyra::EditScriptRegenerateReqStruct` | `lyra::EditScriptRegenerateRespStruct` |
| AIGC 生成 | `lyra` | `GenerateAiMusicMv` | — | `lyra::GenerateAiMusicMvRespStruct` |
| AIGC 生成 | `lyra` | `GenerateAiTextTemplatePackage` | — | `lyra::GenerateAiTextTemplatePackageRespStruct` |
| AIGC 生成 | `lyra` | `GenerateBrushMaskFromVe` | `lyra::GenerateBrushMaskFromVeReqStruct` | `lyra::GenerateBrushMaskFromVeRespStruct` |
| AIGC 生成 | `lyra` | `GenerateFrameTime` | — | `lyra::GenerateFrameTimeRespStruct` |
| AIGC 生成 | `lyra` | `GenerateJson` | `lyra::GenerateJsonReqStruct` | `lyra::GenerateJsonRespStruct` |
| AIGC 生成 | `lyra` | `GenerateOverdubSegments` | — | `lyra::GenerateOverdubSegmentsRespStruct` |
| AIGC 生成 | `lyra` | `GenerateResourcePackage` | — | `lyra::GenerateResourcePackageRespStruct` |
| AIGC 生成 | `lyra` | `GenerateResourcePackageFromDir` | — | `lyra::GenerateResourcePackageFromDirRespStruct` |
| AIGC 生成 | `lyra` | `GenerateTranscriptSegments` | — | `lyra::GenerateTranscriptSegmentsRespStruct` |
| AIGC 生成 | `lyra` | `GetAIClipperInfo` | `lyra::GetAIClipperInfoReqStruct` | `lyra::GetAIClipperInfoRespStruct` |
| AIGC 生成 | `lyra` | `GetAICreateAttachmentData` | `lyra::GetAICreateAttachmentDataReqStruct` | `lyra::GetAICreateAttachmentDataRespStruct` |
| AIGC 生成 | `lyra` | `GetAdScriptDraftFromArticleVideoJson` | — | `lyra::GetAdScriptDraftFromArticleVideoJsonRespStruct` |
| AIGC 生成 | `lyra` | `GetAigcGenerateRecords` | — | `lyra::GetAigcGenerateRecordsRespStruct` |
| AIGC 生成 | `lyra` | `GetAllAigcGenerateItems` | — | `lyra::GetAllAigcGenerateItemsRespStruct` |
| AIGC 生成 | `lyra` | `GetArticleVideoJsonStrFromDraft` | — | `lyra::GetArticleVideoJsonStrFromDraftRespStruct` |
| AIGC 生成 | `lyra` | `GetAttachmentAigcGenerate` | — | `lyra::GetAttachmentAigcGenerateRespStruct` |
| AIGC 生成 | `lyra` | `GetDraftFromArticleVideoJson` | — | `lyra::GetDraftFromArticleVideoJsonRespStruct` |
| AIGC 生成 | `lyra` | `GetDraftFromArticleVideoJsonMergeSame` | — | `lyra::GetDraftFromArticleVideoJsonMergeSameRespStruct` |
| AIGC 生成 | `lyra` | `GetHistoryDraft` | `lyra::GetHistoryDraftReqStruct` | `lyra::GetHistoryDraftRespStruct` |
| AIGC 生成 | `lyra` | `GetHistoryInfo` | `lyra::GetHistoryInfoReqStruct` | `lyra::GetHistoryInfoRespStruct` |
| AIGC 生成 | `lyra` | `GetHistoryMergeChangeNodes` | `lyra::GetHistoryMergeChangeNodesReqStruct` | `lyra::GetHistoryMergeChangeNodesRespStruct` |
| AIGC 生成 | `lyra` | `GetHistoryMgr` | `lyra::GetHistoryMgrReqStruct` | `lyra::GetHistoryMgrRespStruct` |
| AIGC 生成 | `lyra` | `GetLastPreCommitHistory` | `lyra::GetLastPreCommitHistoryReqStruct` | `lyra::GetLastPreCommitHistoryRespStruct` |
| AIGC 生成 | `lyra` | `GetSegmentGenerateAlgorithm` | — | `lyra::GetSegmentGenerateAlgorithmRespStruct` |
| AIGC 生成 | `lyra` | `GetSegmentLastGenerateAlgorithm` | — | `lyra::GetSegmentLastGenerateAlgorithmRespStruct` |
| AIGC 生成 | `lyra` | `GetUndoHistoryIdentifiers` | — | `lyra::GetUndoHistoryIdentifiersRespStruct` |
| AIGC 生成 | `lyra` | `GlobalHistorySwitchTracing` | — | `lyra::GlobalHistorySwitchTracingRespStruct` |
| AIGC 生成 | `lyra` | `GlobalOnDraftHistory` | `lyra::GlobalOnDraftHistoryReqStruct` | `lyra::GlobalOnDraftHistoryRespStruct` |
| AIGC 生成 | `lyra` | `GlobalOnProjectHistoryCallback` | — | `lyra::GlobalOnProjectHistoryCallbackRespStruct` |
| AIGC 生成 | `lyra` | `HandwriteRedo` | — | `lyra::HandwriteRedoRespStruct` |
| AIGC 生成 | `lyra` | `HasAigcWatermark` | — | `lyra::HasAigcWatermarkRespStruct` |
| AIGC 生成 | `lyra` | `HasAudioAigcFeature` | — | `lyra::HasAudioAigcFeatureRespStruct` |
| AIGC 生成 | `lyra` | `ProcessMediaAigc` | `lyra::ProcessMediaAigcReqStruct` | `lyra::ProcessMediaAigcRespStruct` |
| AIGC 生成 | `lyra` | `QueryAIGCWatermarkTimeRangeInfo` | `lyra::QueryAIGCWatermarkTimeRangeInfoReqStruct` | `lyra::QueryAIGCWatermarkTimeRangeInfoRespStruct` |
| AIGC 生成 | `lyra` | `QueryAigcTypesInDraft` | — | `lyra::QueryAigcTypesInDraftRespStruct` |
| AIGC 生成 | `lyra` | `QueryAigcWatermarkTimeRangeInfo` | `lyra::QueryAigcWatermarkTimeRangeInfoReqStruct` | `lyra::QueryAigcWatermarkTimeRangeInfoRespStruct` |
| AIGC 生成 | `lyra` | `QueryCurrentPlayPositionHasAigcWatermark` | — | `lyra::QueryCurrentPlayPositionHasAigcWatermarkRespStruct` |
| AIGC 生成 | `lyra` | `QuerySubDraftAigcWatermarkTimeRangeInfo` | `lyra::QuerySubDraftAigcWatermarkTimeRangeInfoReqStruct` | `lyra::QuerySubDraftAigcWatermarkTimeRangeInfoRespStruct` |
| AIGC 生成 | `lyra` | `RcDeleteAIClipperTranscriptInEditDraft` | `lyra::RcDeleteAIClipperTranscriptInEditDraftReqStruct` | `lyra::RcDeleteAIClipperTranscriptInEditDraftRespStruct` |
| AIGC 生成 | `lyra` | `RcMoveAIClipperTranscriptChapterInEditDraft` | `lyra::RcMoveAIClipperTranscriptChapterInEditDraftReqStruct` | `lyra::RcMoveAIClipperTranscriptChapterInEditDraftRespStruct` |
| AIGC 生成 | `lyra` | `RcMoveAIClipperTranscriptSegmentInEditDraft` | `lyra::RcMoveAIClipperTranscriptSegmentInEditDraftReqStruct` | `lyra::RcMoveAIClipperTranscriptSegmentInEditDraftRespStruct` |
| AIGC 生成 | `lyra` | `RcRestoreAIClipperTranscriptInEditDraft` | `lyra::RcRestoreAIClipperTranscriptInEditDraftReqStruct` | `lyra::RcRestoreAIClipperTranscriptInEditDraftRespStruct` |
| AIGC 生成 | `lyra` | `RcSplitAIClipperTranscriptSegmentInEditDraft` | `lyra::RcSplitAIClipperTranscriptSegmentInEditDraftReqStruct` | `lyra::RcSplitAIClipperTranscriptSegmentInEditDraftRespStruct` |
| AIGC 生成 | `lyra` | `RcTrimAIClipperTranscriptSegmentInEditDraft` | `lyra::RcTrimAIClipperTranscriptSegmentInEditDraftReqStruct` | `lyra::RcTrimAIClipperTranscriptSegmentInEditDraftRespStruct` |
| AIGC 生成 | `lyra` | `RcUnmarkAIClipperTranscriptInEditDraft` | `lyra::RcUnmarkAIClipperTranscriptInEditDraftReqStruct` | `lyra::RcUnmarkAIClipperTranscriptInEditDraftRespStruct` |
| AIGC 生成 | `lyra` | `RecordSubHistory` | — | `lyra::RecordSubHistoryRespStruct` |
| AIGC 生成 | `lyra` | `RemoveAigcPainting` | — | `lyra::RemoveAigcPaintingRespStruct` |
| AIGC 生成 | `lyra` | `RemoveGenerateItem` | — | `lyra::RemoveGenerateItemRespStruct` |
| AIGC 生成 | `lyra` | `RemoveGenerateItemWithoutResult` | — | `lyra::RemoveGenerateItemWithoutResultRespStruct` |
| AIGC 生成 | `lyra` | `ReplaceAICreatorPromptAndMaterial` | — | `lyra::ReplaceAICreatorPromptAndMaterialRespStruct` |
| AIGC 生成 | `lyra` | `ReplaceArticleVideoAllVideos` | `lyra::ReplaceArticleVideoAllVideosReqStruct` | `lyra::ReplaceArticleVideoAllVideosRespStruct` |
| AIGC 生成 | `lyra` | `RestoreAiGenerateTextTemplate` | — | `lyra::RestoreAiGenerateTextTemplateRespStruct` |
| AIGC 生成 | `lyra` | `SaveAICreateAttachment` | — | `lyra::SaveAICreateAttachmentRespStruct` |
| AIGC 生成 | `lyra` | `SeRestoreFromHistoryNode` | — | `lyra::SeRestoreFromHistoryNodeRespStruct` |
| AIGC 生成 | `lyra` | `SetAigcMetaDataCallback` | — | `lyra::SetAigcMetaDataCallbackRespStruct` |
| AIGC 生成 | `lyra` | `SetGenerateCompletionCallback` | — | `lyra::SetGenerateCompletionCallbackRespStruct` |
| AIGC 生成 | `lyra` | `SetGenerateProgressCallback` | — | `lyra::SetGenerateProgressCallbackRespStruct` |
| AIGC 生成 | `lyra` | `SetGlobalHistoryStatusFetcher` | `lyra::SetGlobalHistoryStatusFetcherReqStruct` | `lyra::SetGlobalHistoryStatusFetcherRespStruct` |
| AIGC 生成 | `lyra` | `StartAIGCTask` | `lyra::StartAIGCTaskReqStruct` | `lyra::StartAIGCTaskRespStruct` |
| AIGC 生成 | `lyra` | `StartGenerate` | — | `lyra::StartGenerateRespStruct` |
| AIGC 生成 | `lyra` | `StartHistoryTracing` | `lyra::StartHistoryTracingReqStruct` | `lyra::StartHistoryTracingRespStruct` |
| AIGC 生成 | `lyra` | `StopHistoryTracing` | `lyra::StopHistoryTracingReqStruct` | `lyra::StopHistoryTracingRespStruct` |
| AIGC 生成 | `lyra` | `UpdateAICreatorMaterialIds` | — | `lyra::UpdateAICreatorMaterialIdsRespStruct` |
| AIGC 生成 | `lyra` | `UpdateAICreatorPromptInfo` | — | `lyra::UpdateAICreatorPromptInfoRespStruct` |
| AIGC 生成 | `lyra` | `UpdateAICreatorPromptInfoSceneContext` | — | `lyra::UpdateAICreatorPromptInfoSceneContextRespStruct` |
| AIGC 生成 | `lyra` | `UpdateAICreatorSceneType` | — | `lyra::UpdateAICreatorSceneTypeRespStruct` |
| AIGC 生成 | `lyra` | `UpdateAIGCPreviewWatermark` | — | `lyra::UpdateAIGCPreviewWatermarkRespStruct` |
| AIGC 生成 | `lyra` | `UpdateAIGCWatermark` | — | `lyra::UpdateAIGCWatermarkRespStruct` |
| AIGC 生成 | `lyra` | `UpdateAIGCWatermarkNewVersion` | — | `lyra::UpdateAIGCWatermarkNewVersionRespStruct` |
| AIGC 生成 | `lyra` | `UpdateAITransitionHistory` | — | `lyra::UpdateAITransitionHistoryRespStruct` |
| AIGC 生成 | `lyra` | `UpdateAiGenerateTextTemplateAdjustParam` | — | `lyra::UpdateAiGenerateTextTemplateAdjustParamRespStruct` |
| AIGC 生成 | `lyra` | `UpdateAiGenerateTextTemplateText` | — | `lyra::UpdateAiGenerateTextTemplateTextRespStruct` |
| AIGC 生成 | `lyra` | `UpdateAigcEffectArtifactPath` | `lyra::UpdateAigcEffectArtifactPathReqStruct` | `lyra::UpdateAigcEffectArtifactPathRespStruct` |
| AIGC 生成 | `lyra` | `UpdateAigcSegment` | — | `lyra::UpdateAigcSegmentRespStruct` |
| AIGC 生成 | `lyra` | `UpdateAigcWatermarkLocation` | — | `lyra::UpdateAigcWatermarkLocationRespStruct` |
| AIGC 生成 | `lyra` | `UpdateArticleVideoShot` | — | `lyra::UpdateArticleVideoShotRespStruct` |
| AIGC 生成 | `lyra` | `UpdateSegmentGenerateItemOrder` | — | `lyra::UpdateSegmentGenerateItemOrderRespStruct` |
| AIGC 生成 | `lyra` | `UpdateSegmentGenerateStatus` | — | `lyra::UpdateSegmentGenerateStatusRespStruct` |
| AIGC 生成 | `lyra` | `VideoSetVideoAigcType` | `lyra::VideoSetVideoAigcTypeReqStruct` | `lyra::VideoSetVideoAigcTypeRespStruct` |
| 人脸 | `lyra` | `CancelMultFacesEffect` | `lyra::CancelMultFacesEffectReqStruct` | `lyra::CancelMultFacesEffectRespStruct` |
| 人脸 | `lyra` | `DetectFirstFaceFrame` | — | `lyra::DetectFirstFaceFrameRespStruct` |
| 人脸 | `lyra` | `EnableEffectFaceRecognition` | — | `lyra::EnableEffectFaceRecognitionRespStruct` |
| 人脸 | `lyra` | `EnableMultFacesEffect` | `lyra::EnableMultFacesEffectReqStruct` | `lyra::EnableMultFacesEffectRespStruct` |
| 人脸 | `lyra` | `EnableVideoFaceRecognition` | — | `lyra::EnableVideoFaceRecognitionRespStruct` |
| 人脸 | `lyra` | `GetEffectFaceBoundingBoxInfos` | — | `lyra::GetEffectFaceBoundingBoxInfosRespStruct` |
| 人脸 | `lyra` | `GetEffectFaceBoundingBoxInfosWithCb` | — | `lyra::GetEffectFaceBoundingBoxInfosWithCbRespStruct` |
| 人脸 | `lyra` | `GetFaceBoundingBoxInfos` | — | `lyra::GetFaceBoundingBoxInfosRespStruct` |
| 人脸 | `lyra` | `GetTrackerSurfaceBox` | — | `lyra::GetTrackerSurfaceBoxRespStruct` |
| 人脸 | `lyra` | `GetTrackerSurfacePosition` | — | `lyra::GetTrackerSurfacePositionRespStruct` |
| 人脸 | `lyra` | `GetVideoFaceBoundingBoxInfos` | `lyra::GetVideoFaceBoundingBoxInfosReqStruct` | `lyra::GetVideoFaceBoundingBoxInfosRespStruct` |
| 人脸 | `lyra` | `InitVideoFaceRecognitionPath` | `lyra::InitVideoFaceRecognitionPathReqStruct` | `lyra::InitVideoFaceRecognitionPathRespStruct` |
| 人脸 | `lyra` | `IsAiFaceOcclusionEffectWithRootPath` | `lyra::IsAiFaceOcclusionEffectWithRootPathReqStruct` | `lyra::IsAiFaceOcclusionEffectWithRootPathRespStruct` |
| 人脸 | `lyra` | `IsMultiFacesEffectWithRootPath` | `lyra::IsMultiFacesEffectWithRootPathReqStruct` | `lyra::IsMultiFacesEffectWithRootPathRespStruct` |
| 人脸 | `lyra` | `NotifyMediaFaceBodyFinish` | — | `lyra::NotifyMediaFaceBodyFinishRespStruct` |
| 人脸 | `lyra` | `SetMagnifierSurface` | — | `lyra::SetMagnifierSurfaceRespStruct` |
| 人脸 | `lyra` | `SetPreviewSurfaceImage` | — | `lyra::SetPreviewSurfaceImageRespStruct` |
| 人脸 | `lyra` | `SetPreviewSurfaceImageToken` | — | `lyra::SetPreviewSurfaceImageTokenRespStruct` |
| 人脸 | `lyra` | `SetSurface` | — | `lyra::SetSurfaceRespStruct` |
| 人脸 | `lyra` | `SetSurfaceAsync` | — | `lyra::SetSurfaceAsyncRespStruct` |
| 人脸 | `lyra` | `SetVideoFaceRecognitionPath` | `lyra::SetVideoFaceRecognitionPathReqStruct` | `lyra::SetVideoFaceRecognitionPathRespStruct` |
| 其它 | `lyra` | `AddHandwrite` | — | `lyra::AddHandwriteRespStruct` |
| 其它 | `lyra` | `UpdateSubDraftNewTextTemplateCanvas` | — | `lyra::UpdateSubDraftNewTextTemplateCanvasRespStruct` |
| 字幕/文本 | `lyra` | `AddCaptionAnim` | — | `lyra::AddCaptionAnimRespStruct` |
| 字幕/文本 | `lyra` | `AddDigitalHumanTemplateSubtitles` | — | `lyra::AddDigitalHumanTemplateSubtitlesRespStruct` |
| 字幕/文本 | `lyra` | `AddTranscriptEditWordsSyncSubtitle` | `lyra::AddTranscriptEditWordsSyncSubtitleReqStruct` | `lyra::AddTranscriptEditWordsSyncSubtitleRespStruct` |
| 字幕/文本 | `lyra` | `AvoidBilingualCaptionOverlap` | — | `lyra::AvoidBilingualCaptionOverlapRespStruct` |
| 字幕/文本 | `lyra` | `BatchReplaceTextTemplateSubtitleText` | — | `lyra::BatchReplaceTextTemplateSubtitleTextRespStruct` |
| 字幕/文本 | `lyra` | `CheckIsMixCaptionSegments` | — | `lyra::CheckIsMixCaptionSegmentsRespStruct` |
| 字幕/文本 | `lyra` | `ClearSubtitleFragmentInfos` | `lyra::ClearSubtitleFragmentInfosReqStruct` | `lyra::ClearSubtitleFragmentInfosRespStruct` |
| 字幕/文本 | `lyra` | `CopyTextTemplateSubtitle` | — | `lyra::CopyTextTemplateSubtitleRespStruct` |
| 字幕/文本 | `lyra` | `CreateSubtitleFragmentInfos` | — | `lyra::CreateSubtitleFragmentInfosRespStruct` |
| 字幕/文本 | `lyra` | `CreateTranscriptEditSubtitle` | `lyra::CreateTranscriptEditSubtitleReqStruct` | `lyra::CreateTranscriptEditSubtitleRespStruct` |
| 字幕/文本 | `lyra` | `GenerateSubtitleData` | — | `lyra::GenerateSubtitleDataRespStruct` |
| 字幕/文本 | `lyra` | `GenerateTranscriptSegmentsForSubtitle` | — | `lyra::GenerateTranscriptSegmentsForSubtitleRespStruct` |
| 字幕/文本 | `lyra` | `GetSubTitleData` | — | `lyra::GetSubTitleDataRespStruct` |
| 字幕/文本 | `lyra` | `GetSubtitleSpacing` | — | `lyra::GetSubtitleSpacingRespStruct` |
| 字幕/文本 | `lyra` | `ImportCaption` | — | `lyra::ImportCaptionRespStruct` |
| 字幕/文本 | `lyra` | `InitTranscriptEditAttachmentBySubtitle` | `lyra::InitTranscriptEditAttachmentBySubtitleReqStruct` | `lyra::InitTranscriptEditAttachmentBySubtitleRespStruct` |
| 字幕/文本 | `lyra` | `MatchCaptionTimeline` | — | `lyra::MatchCaptionTimelineRespStruct` |
| 字幕/文本 | `lyra` | `MergeCaptionKeyWordStyles` | — | `lyra::MergeCaptionKeyWordStylesRespStruct` |
| 字幕/文本 | `lyra` | `ModifyTextSubtitleBatchConfig` | — | `lyra::ModifyTextSubtitleBatchConfigRespStruct` |
| 字幕/文本 | `lyra` | `RemoveMutilSubtitleSegment` | — | `lyra::RemoveMutilSubtitleSegmentRespStruct` |
| 字幕/文本 | `lyra` | `RemoveTranscriptEditWordsSyncSubtitle` | — | `lyra::RemoveTranscriptEditWordsSyncSubtitleRespStruct` |
| 字幕/文本 | `lyra` | `ReplaceSubtitleText` | `lyra::ReplaceSubtitleTextReqStruct` | `lyra::ReplaceSubtitleTextRespStruct` |
| 字幕/文本 | `lyra` | `ResetSubTitleGroupId` | — | `lyra::ResetSubTitleGroupIdRespStruct` |
| 字幕/文本 | `lyra` | `ResetSubtitleTemplate` | `lyra::ResetSubtitleTemplateReqStruct` | `lyra::ResetSubtitleTemplateRespStruct` |
| 字幕/文本 | `lyra` | `SetCaptionTextCase` | — | `lyra::SetCaptionTextCaseRespStruct` |
| 字幕/文本 | `lyra` | `SplitSubtitleFragmentInfos` | — | `lyra::SplitSubtitleFragmentInfosRespStruct` |
| 字幕/文本 | `lyra` | `SplitSubtitleFragmentInfosStatic` | — | `lyra::SplitSubtitleFragmentInfosStaticRespStruct` |
| 字幕/文本 | `lyra` | `UpdateCaptionAnim` | — | `lyra::UpdateCaptionAnimRespStruct` |
| 字幕/文本 | `lyra` | `UpdateCaptionAnimExpression` | — | `lyra::UpdateCaptionAnimExpressionRespStruct` |
| 字幕/文本 | `lyra` | `UpdateCaptionFragment` | — | `lyra::UpdateCaptionFragmentRespStruct` |
| 字幕/文本 | `lyra` | `UpdateCaptionKeyWordStyleUnbundling` | — | `lyra::UpdateCaptionKeyWordStyleUnbundlingRespStruct` |
| 字幕/文本 | `lyra` | `UpdateCaptionKeywordStyle` | — | `lyra::UpdateCaptionKeywordStyleRespStruct` |
| 字幕/文本 | `lyra` | `UpdateCaptionKeywords` | — | `lyra::UpdateCaptionKeywordsRespStruct` |
| 字幕/文本 | `lyra` | `UpdateKeywordStyle` | `lyra::UpdateKeywordStyleReqStruct` | `lyra::UpdateKeywordStyleRespStruct` |
| 字幕/文本 | `lyra` | `UpdatePartBySubtitleJson` | — | `lyra::UpdatePartBySubtitleJsonRespStruct` |
| 字幕/文本 | `lyra` | `UpdateScriptAndSubTitle` | — | `lyra::UpdateScriptAndSubTitleRespStruct` |
| 字幕/文本 | `lyra` | `UpdateSentenceSubtitleSegId` | `lyra::UpdateSentenceSubtitleSegIdReqStruct` | `lyra::UpdateSentenceSubtitleSegIdRespStruct` |
| 字幕/文本 | `lyra` | `UpdateSubtitleFragmentInfos` | — | `lyra::UpdateSubtitleFragmentInfosRespStruct` |
| 字幕/文本 | `lyra` | `UpdateSubtitleFragmentTimerange` | `lyra::UpdateSubtitleFragmentTimerangeReqStruct` | `lyra::UpdateSubtitleFragmentTimerangeRespStruct` |
| 字幕/文本 | `lyra` | `UpdateSubtitleKeywords` | `lyra::UpdateSubtitleKeywordsReqStruct` | `lyra::UpdateSubtitleKeywordsRespStruct` |
| 字幕/文本 | `lyra` | `UpdateSubtitleTemplate` | — | `lyra::UpdateSubtitleTemplateRespStruct` |
| 字幕/文本 | `lyra` | `UpdateSubtitleTextSegmentAddSource` | — | `lyra::UpdateSubtitleTextSegmentAddSourceRespStruct` |
| 字幕/文本 | `lyra` | `UpdateTextTemplateKeywordStyle` | `lyra::UpdateTextTemplateKeywordStyleReqStruct` | `lyra::UpdateTextTemplateKeywordStyleRespStruct` |
| 字幕/文本 | `lyra` | `UpdateTextTemplateSubtitleKeywords` | `lyra::UpdateTextTemplateSubtitleKeywordsReqStruct` | `lyra::UpdateTextTemplateSubtitleKeywordsRespStruct` |
| 抠像/分割 | `lyra` | `AddCustomMatting` | `lyra::AddCustomMattingReqStruct` | `lyra::AddCustomMattingRespStruct` |
| 抠像/分割 | `lyra` | `AddMatting` | `lyra::AddMattingReqStruct` | `lyra::AddMattingRespStruct` |
| 抠像/分割 | `lyra` | `AddMattingListener` | — | `lyra::AddMattingListenerRespStruct` |
| 抠像/分割 | `lyra` | `AdjustDigitalHumanSpeaker` | — | `lyra::AdjustDigitalHumanSpeakerRespStruct` |
| 抠像/分割 | `lyra` | `CheckMattingNeedRestore` | — | `lyra::CheckMattingNeedRestoreRespStruct` |
| 抠像/分割 | `lyra` | `ChromaVideo` | `lyra::ChromaVideoReqStruct` | `lyra::ChromaVideoRespStruct` |
| 抠像/分割 | `lyra` | `CopyCustomMattingResult` | — | `lyra::CopyCustomMattingResultRespStruct` |
| 抠像/分割 | `lyra` | `CopyMattingDataOnMattingEdit` | — | `lyra::CopyMattingDataOnMattingEditRespStruct` |
| 抠像/分割 | `lyra` | `EnterAdjustChromaPick` | `lyra::EnterAdjustChromaPickReqStruct` | `lyra::EnterAdjustChromaPickRespStruct` |
| 抠像/分割 | `lyra` | `EnterVideoChromaPick` | `lyra::EnterVideoChromaPickReqStruct` | `lyra::EnterVideoChromaPickRespStruct` |
| 抠像/分割 | `lyra` | `ExportCurrentMattingFrame` | — | `lyra::ExportCurrentMattingFrameRespStruct` |
| 抠像/分割 | `lyra` | `GetLvMattingPhotoUseNewModel` | — | `lyra::GetLvMattingPhotoUseNewModelRespStruct` |
| 抠像/分割 | `lyra` | `GetLvMattingVideoUseNewModel` | — | `lyra::GetLvMattingVideoUseNewModelRespStruct` |
| 抠像/分割 | `lyra` | `GetPortraitAlgorithmCacheOptEnable` | — | `lyra::GetPortraitAlgorithmCacheOptEnableRespStruct` |
| 抠像/分割 | `lyra` | `GetSegmentMattingInfo` | — | `lyra::GetSegmentMattingInfoRespStruct` |
| 抠像/分割 | `lyra` | `LeaveAdjustChromaPick` | `lyra::LeaveAdjustChromaPickReqStruct` | `lyra::LeaveAdjustChromaPickRespStruct` |
| 抠像/分割 | `lyra` | `LeaveVideoChromaPick` | `lyra::LeaveVideoChromaPickReqStruct` | `lyra::LeaveVideoChromaPickRespStruct` |
| 抠像/分割 | `lyra` | `PrepareMatting` | — | `lyra::PrepareMattingRespStruct` |
| 抠像/分割 | `lyra` | `RefreshAllVideoChromaFilter` | `lyra::RefreshAllVideoChromaFilterReqStruct` | `lyra::RefreshAllVideoChromaFilterRespStruct` |
| 抠像/分割 | `lyra` | `RemoveMattingListener` | — | `lyra::RemoveMattingListenerRespStruct` |
| 抠像/分割 | `lyra` | `RemoveMattingTask` | `lyra::RemoveMattingTaskReqStruct` | `lyra::RemoveMattingTaskRespStruct` |
| 抠像/分割 | `lyra` | `RestoreMattingFromDraft` | — | `lyra::RestoreMattingFromDraftRespStruct` |
| 抠像/分割 | `lyra` | `SetChromaColor` | `lyra::SetChromaColorReqStruct` | `lyra::SetChromaColorRespStruct` |
| 抠像/分割 | `lyra` | `SetChromaEdgeSmooth` | `lyra::SetChromaEdgeSmoothReqStruct` | `lyra::SetChromaEdgeSmoothRespStruct` |
| 抠像/分割 | `lyra` | `SetChromaIntensity` | `lyra::SetChromaIntensityReqStruct` | `lyra::SetChromaIntensityRespStruct` |
| 抠像/分割 | `lyra` | `SetChromaShadow` | `lyra::SetChromaShadowReqStruct` | `lyra::SetChromaShadowRespStruct` |
| 抠像/分割 | `lyra` | `SetChromaSpill` | `lyra::SetChromaSpillReqStruct` | `lyra::SetChromaSpillRespStruct` |
| 抠像/分割 | `lyra` | `SetMattingCachePath` | — | `lyra::SetMattingCachePathRespStruct` |
| 抠像/分割 | `lyra` | `StopMattingTaskBeforeInteractive` | — | `lyra::StopMattingTaskBeforeInteractiveRespStruct` |
| 抠像/分割 | `lyra` | `TemplateVideoAiMattingApply` | `lyra::TemplateVideoAiMattingApplyReqStruct` | `lyra::TemplateVideoAiMattingApplyRespStruct` |
| 抠像/分割 | `lyra` | `UpdateMatting` | — | `lyra::UpdateMattingRespStruct` |
| 抠像/分割 | `lyra` | `UpdateVideoAiMattingApply` | — | `lyra::UpdateVideoAiMattingApplyRespStruct` |
| 抠像/分割 | `lyra` | `UpdateVideoMattingWithFlagPath` | — | `lyra::UpdateVideoMattingWithFlagPathRespStruct` |
| 抠像/分割 | `lyra` | `UpdateVideoMattingWithToggle` | — | `lyra::UpdateVideoMattingWithToggleRespStruct` |
| 抠像/分割 | `lyra` | `VideoAiMattingToggle` | `lyra::VideoAiMattingToggleReqStruct` | `lyra::VideoAiMattingToggleRespStruct` |
| 抠像/分割 | `lyra` | `WaitForCustomMatting` | `lyra::WaitForCustomMattingReqStruct` | `lyra::WaitForCustomMattingRespStruct` |
| 智能剪辑决策 | `clipflow` | `AddClipflowNodeHooker` | — | `clipflow::AddClipflowNodeHookerRespStruct` |
| 智能剪辑决策 | `clipflow` | `AddClipflowTaskHooker` | — | `clipflow::AddClipflowTaskHookerRespStruct` |
| 智能剪辑决策 | `lyra` | `AddScenes` | — | `lyra::AddScenesRespStruct` |
| 智能剪辑决策 | `lyra` | `AppendClipFlowAsyncTaskListenerProxy` | — | `lyra::AppendClipFlowAsyncTaskListenerProxyRespStruct` |
| 智能剪辑决策 | `lyra` | `ApplySegmentSmartEdit` | — | `lyra::ApplySegmentSmartEditRespStruct` |
| 智能剪辑决策 | `lyra` | `ApplySmartCrop` | `lyra::ApplySmartCropReqStruct` | `lyra::ApplySmartCropRespStruct` |
| 智能剪辑决策 | `lyra` | `ApplyTextSmartSplit` | — | `lyra::ApplyTextSmartSplitRespStruct` |
| 智能剪辑决策 | `lyra` | `ApplyTextTemplateSmartSplit` | — | `lyra::ApplyTextTemplateSmartSplitRespStruct` |
| 智能剪辑决策 | `lyra` | `CancelRunningSmartCropAlgorithm` | — | `lyra::CancelRunningSmartCropAlgorithmRespStruct` |
| 智能剪辑决策 | `lyra` | `CancelVideoHighlightcutProcess` | — | `lyra::CancelVideoHighlightcutProcessRespStruct` |
| 智能剪辑决策 | `clipflow` | `ClipflowNode` | `clipflow::ClipflowNodeReq` | `clipflow::ClipflowNodeResp` |
| 智能剪辑决策 | `lyra` | `CopyHighLightSegment` | `lyra::CopyHighLightSegmentReqStruct` | `lyra::CopyHighLightSegmentRespStruct` |
| 智能剪辑决策 | `clipflow` | `CreateClipFlowNode` | — | `clipflow::CreateClipFlowNodeRespStruct` |
| 智能剪辑决策 | `clipflow` | `DecisionNode` | — | `clipflow::DecisionNodeResp` |
| 智能剪辑决策 | `lyra` | `GetAiMaterialClipflowEnable` | — | `lyra::GetAiMaterialClipflowEnableRespStruct` |
| 智能剪辑决策 | `lyra` | `GetAlgorithmCacheProgressSnapshot` | — | `lyra::GetAlgorithmCacheProgressSnapshotRespStruct` |
| 智能剪辑决策 | `lyra` | `GetAllFeatureSceneSegment` | `lyra::GetAllFeatureSceneSegmentReqStruct` | `lyra::GetAllFeatureSceneSegmentRespStruct` |
| 智能剪辑决策 | `lyra` | `GetAllRemovedSceneSegment` | — | `lyra::GetAllRemovedSceneSegmentRespStruct` |
| 智能剪辑决策 | `lyra` | `GetAllResourceSceneSegment` | — | `lyra::GetAllResourceSceneSegmentRespStruct` |
| 智能剪辑决策 | `lyra` | `GetAllSegmentScene` | — | `lyra::GetAllSegmentSceneRespStruct` |
| 智能剪辑决策 | `lyra` | `GetClipflowEngineAbtest` | `lyra::GetClipflowEngineAbtestReqStruct` | `lyra::GetClipflowEngineAbtestRespStruct` |
| 智能剪辑决策 | `lyra` | `GetSceneTagAttachment` | — | `lyra::GetSceneTagAttachmentRespStruct` |
| 智能剪辑决策 | `lyra` | `GetSegmentShotInfo` | — | `lyra::GetSegmentShotInfoRespStruct` |
| 智能剪辑决策 | `lyra` | `GetSmartMask` | — | `lyra::GetSmartMaskRespStruct` |
| 智能剪辑决策 | `clipflow` | `NotifyAsyncResult` | `clipflow::NotifyAsyncResultReqStruct` | — |
| 智能剪辑决策 | `clipflow` | `QueryClipFlowTask` | `clipflow::QueryClipFlowTaskReqStruct` | — |
| 智能剪辑决策 | `lyra` | `QuerySceneTagByAlgorithm` | — | `lyra::QuerySceneTagByAlgorithmRespStruct` |
| 智能剪辑决策 | `lyra` | `QuerySceneTagByFeature` | `lyra::QuerySceneTagByFeatureReqStruct` | `lyra::QuerySceneTagByFeatureRespStruct` |
| 智能剪辑决策 | `lyra` | `QuerySceneTagByResource` | `lyra::QuerySceneTagByResourceReqStruct` | `lyra::QuerySceneTagByResourceRespStruct` |
| 智能剪辑决策 | `lyra` | `QuerySceneTagOfSegment` | — | `lyra::QuerySceneTagOfSegmentRespStruct` |
| 智能剪辑决策 | `lyra` | `RecordSceneTagByFeature` | — | `lyra::RecordSceneTagByFeatureRespStruct` |
| 智能剪辑决策 | `lyra` | `RecordSceneTagByResource` | — | `lyra::RecordSceneTagByResourceRespStruct` |
| 智能剪辑决策 | `lyra` | `RecordSceneTagOfSegment` | — | `lyra::RecordSceneTagOfSegmentRespStruct` |
| 智能剪辑决策 | `clipflow` | `RegisterNodeCacheImpl` | — | `clipflow::RegisterNodeCacheImplRespStruct` |
| 智能剪辑决策 | `lyra` | `RemoveSceneTagOfSegment` | — | `lyra::RemoveSceneTagOfSegmentRespStruct` |
| 智能剪辑决策 | `lyra` | `RemoveScenes` | — | `lyra::RemoveScenesRespStruct` |
| 智能剪辑决策 | `lyra` | `RemoveSmartCrop` | `lyra::RemoveSmartCropReqStruct` | `lyra::RemoveSmartCropRespStruct` |
| 智能剪辑决策 | `lyra` | `RemoveTempSmartCropParam` | `lyra::RemoveTempSmartCropParamReqStruct` | `lyra::RemoveTempSmartCropParamRespStruct` |
| 智能剪辑决策 | `lyra` | `ReplaceScenes` | — | `lyra::ReplaceScenesRespStruct` |
| 智能剪辑决策 | `lyra` | `ResetGlobalSmartColorAdjust` | `lyra::ResetGlobalSmartColorAdjustReqStruct` | `lyra::ResetGlobalSmartColorAdjustRespStruct` |
| 智能剪辑决策 | `lyra` | `ResetSmartColorAdjust` | `lyra::ResetSmartColorAdjustReqStruct` | `lyra::ResetSmartColorAdjustRespStruct` |
| 智能剪辑决策 | `lyra` | `RunSmartCropAlgorithm` | — | `lyra::RunSmartCropAlgorithmRespStruct` |
| 智能剪辑决策 | `lyra` | `SetSmartComplementFrame` | — | `lyra::SetSmartComplementFrameRespStruct` |
| 智能剪辑决策 | `lyra` | `SetSmartMatchVideos` | — | `lyra::SetSmartMatchVideosRespStruct` |
| 智能剪辑决策 | `lyra` | `SetVideoSmartMatchInfo` | — | `lyra::SetVideoSmartMatchInfoRespStruct` |
| 智能剪辑决策 | `lyra` | `SmartColorAdjustEnable` | `lyra::SmartColorAdjustEnableReqStruct` | `lyra::SmartColorAdjustEnableRespStruct` |
| 智能剪辑决策 | `lyra` | `StartVideoHighlightcutProcess` | — | `lyra::StartVideoHighlightcutProcessRespStruct` |
| 智能剪辑决策 | `lyra` | `SupplementSceneTagAttachment` | `lyra::SupplementSceneTagAttachmentReqStruct` | `lyra::SupplementSceneTagAttachmentRespStruct` |
| 智能剪辑决策 | `clipflow` | `UndoRedoTasks` | `clipflow::UndoRedoTasksReqStruct` | — |
| 智能剪辑决策 | `lyra` | `UpdateSmartAdsInfo` | — | `lyra::UpdateSmartAdsInfoRespStruct` |
| 智能剪辑决策 | `lyra` | `UpdateSmartCropApplySource` | — | `lyra::UpdateSmartCropApplySourceRespStruct` |
| 智能剪辑决策 | `lyra` | `UpdateSmartCropParam` | `lyra::UpdateSmartCropParamReqStruct` | `lyra::UpdateSmartCropParamRespStruct` |
| 画质 | `lyra` | `AudioEnhance` | `lyra::AudioEnhanceReqStruct` | `lyra::AudioEnhanceRespStruct` |
| 画质 | `lyra` | `AudioRealtimeDenoise` | `lyra::AudioRealtimeDenoiseReqStruct` | `lyra::AudioRealtimeDenoiseRespStruct` |
| 画质 | `lyra` | `AutoAlignDraftFrameTimeWithDraft` | — | `lyra::AutoAlignDraftFrameTimeWithDraftRespStruct` |
| 画质 | `lyra` | `CancelDeflicker` | `lyra::CancelDeflickerReqStruct` | `lyra::CancelDeflickerRespStruct` |
| 画质 | `lyra` | `CancelQualityEnhance` | `lyra::CancelQualityEnhanceReqStruct` | `lyra::CancelQualityEnhanceRespStruct` |
| 画质 | `lyra` | `CancelRunSmartRelightAlgorithm` | `lyra::CancelRunSmartRelightAlgorithmReqStruct` | `lyra::CancelRunSmartRelightAlgorithmRespStruct` |
| 画质 | `lyra` | `CancelSuperResolution` | `lyra::CancelSuperResolutionReqStruct` | `lyra::CancelSuperResolutionRespStruct` |
| 画质 | `lyra` | `ClearSmartRelightCache` | — | `lyra::ClearSmartRelightCacheRespStruct` |
| 画质 | `lyra` | `ConvertRelightInfoFromDraft` | — | `lyra::ConvertRelightInfoFromDraftRespStruct` |
| 画质 | `lyra` | `ConvertRelightInfoFromJson` | — | `lyra::ConvertRelightInfoFromJsonRespStruct` |
| 画质 | `lyra` | `DelSmartRelight` | `lyra::DelSmartRelightReqStruct` | `lyra::DelSmartRelightRespStruct` |
| 画质 | `lyra` | `EnhanceVideo` | `lyra::EnhanceVideoReqStruct` | `lyra::EnhanceVideoRespStruct` |
| 画质 | `lyra` | `FixSegmentResourceWithDraft` | — | `lyra::FixSegmentResourceWithDraftRespStruct` |
| 画质 | `lyra` | `GetDeflickerPath` | — | `lyra::GetDeflickerPathRespStruct` |
| 画质 | `lyra` | `GetDraftResourcesWithDraft` | — | `lyra::GetDraftResourcesWithDraftRespStruct` |
| 画质 | `lyra` | `GetQualityEnhancePath` | — | `lyra::GetQualityEnhancePathRespStruct` |
| 画质 | `lyra` | `GetSuperResolutionPath` | — | `lyra::GetSuperResolutionPathRespStruct` |
| 画质 | `lyra` | `HdrVividEnable` | `lyra::HdrVividEnableReqStruct` | `lyra::HdrVividEnableRespStruct` |
| 画质 | `lyra` | `InitSinglePlayerWithDraft` | — | `lyra::InitSinglePlayerWithDraftRespStruct` |
| 画质 | `lyra` | `InitSmartRelightDefaultSettings` | — | `lyra::InitSmartRelightDefaultSettingsRespStruct` |
| 画质 | `lyra` | `IsHdrSupported` | — | `lyra::IsHdrSupportedRespStruct` |
| 画质 | `lyra` | `IsSmartRelightCacheFinished` | — | `lyra::IsSmartRelightCacheFinishedRespStruct` |
| 画质 | `lyra` | `IsSmartRelightComplete` | — | `lyra::IsSmartRelightCompleteRespStruct` |
| 画质 | `lyra` | `IsSupportSuperResolution` | — | `lyra::IsSupportSuperResolutionRespStruct` |
| 画质 | `lyra` | `MakeSmartRelightCacheDir` | — | `lyra::MakeSmartRelightCacheDirRespStruct` |
| 画质 | `lyra` | `NotifyQualityEnhanceComplete` | `lyra::NotifyQualityEnhanceCompleteReqStruct` | `lyra::NotifyQualityEnhanceCompleteRespStruct` |
| 画质 | `lyra` | `NotifySuperResolutionComplete` | `lyra::NotifySuperResolutionCompleteReqStruct` | `lyra::NotifySuperResolutionCompleteRespStruct` |
| 画质 | `lyra` | `PauseDeflicker` | — | `lyra::PauseDeflickerRespStruct` |
| 画质 | `lyra` | `PauseInterpolationVideo` | — | `lyra::PauseInterpolationVideoRespStruct` |
| 画质 | `lyra` | `PauseSmartRelight` | — | `lyra::PauseSmartRelightRespStruct` |
| 画质 | `lyra` | `ResumeDeflicker` | — | `lyra::ResumeDeflickerRespStruct` |
| 画质 | `lyra` | `ResumeInterpolationVideo` | — | `lyra::ResumeInterpolationVideoRespStruct` |
| 画质 | `lyra` | `RunQualityEnhanceAlgorithm` | `lyra::RunQualityEnhanceAlgorithmReqStruct` | `lyra::RunQualityEnhanceAlgorithmRespStruct` |
| 画质 | `lyra` | `RunSmartRelightAlgorithm` | `lyra::RunSmartRelightAlgorithmReqStruct` | `lyra::RunSmartRelightAlgorithmRespStruct` |
| 画质 | `lyra` | `ScaleComposition` | — | `lyra::ScaleCompositionRespStruct` |
| 画质 | `lyra` | `ScaleCoverSegment` | — | `lyra::ScaleCoverSegmentRespStruct` |
| 画质 | `lyra` | `ScaleSegment` | `lyra::ScaleSegmentReqStruct` | `lyra::ScaleSegmentRespStruct` |
| 画质 | `lyra` | `ScaleText` | `lyra::ScaleTextReqStruct` | `lyra::ScaleTextRespStruct` |
| 画质 | `lyra` | `ScaleTextLayer` | `lyra::ScaleTextLayerReqStruct` | `lyra::ScaleTextLayerRespStruct` |
| 画质 | `lyra` | `SetDenoiseModelPath` | — | `lyra::SetDenoiseModelPathRespStruct` |
| 画质 | `lyra` | `SetHdrSettings` | `lyra::SetHdrSettingsReqStruct` | `lyra::SetHdrSettingsRespStruct` |
| 画质 | `lyra` | `SetQualityEnhance` | `lyra::SetQualityEnhanceReqStruct` | `lyra::SetQualityEnhanceRespStruct` |
| 画质 | `lyra` | `SetSegmentUniformScale` | `lyra::SetSegmentUniformScaleReqStruct` | `lyra::SetSegmentUniformScaleRespStruct` |
| 画质 | `lyra` | `SetSuperResolution` | — | `lyra::SetSuperResolutionRespStruct` |
| 画质 | `lyra` | `SingleResourcePlayerOnHDRUnsupported` | — | `lyra::SingleResourcePlayerOnHDRUnsupportedRespStruct` |
| 画质 | `lyra` | `StartConvertDeflicker` | `lyra::StartConvertDeflickerReqStruct` | `lyra::StartConvertDeflickerRespStruct` |
| 画质 | `lyra` | `StartConvertQualityEnhance` | `lyra::StartConvertQualityEnhanceReqStruct` | `lyra::StartConvertQualityEnhanceRespStruct` |
| 画质 | `lyra` | `StartConvertSuperResolution` | `lyra::StartConvertSuperResolutionReqStruct` | `lyra::StartConvertSuperResolutionRespStruct` |
| 画质 | `lyra` | `UpdateDraftCanvasScale` | — | `lyra::UpdateDraftCanvasScaleRespStruct` |
| 画质 | `lyra` | `UpdateGreenScale` | — | `lyra::UpdateGreenScaleRespStruct` |
| 画质 | `lyra` | `UpdateSmartRelight` | `lyra::UpdateSmartRelightReqStruct` | `lyra::UpdateSmartRelightRespStruct` |
| 画质 | `lyra` | `UpdateSmartRelightAlgorithmParam` | `lyra::UpdateSmartRelightAlgorithmParamReqStruct` | `lyra::UpdateSmartRelightAlgorithmParamRespStruct` |
| 画质 | `lyra` | `UpdateSubDraftSegmentScale` | — | `lyra::UpdateSubDraftSegmentScaleRespStruct` |
| 画质 | `lyra` | `VideoDeflicker` | `lyra::VideoDeflickerReqStruct` | `lyra::VideoDeflickerRespStruct` |
| 画质 | `lyra` | `VideoRealtimeDenoise` | `lyra::VideoRealtimeDenoiseReqStruct` | `lyra::VideoRealtimeDenoiseRespStruct` |
| 画质 | `lyra` | `VideoScaleToAll` | `lyra::VideoScaleToAllReqStruct` | `lyra::VideoScaleToAllRespStruct` |
| 画质 | `lyra` | `VideoUpdateHdrSettings` | `lyra::VideoUpdateHdrSettingsReqStruct` | `lyra::VideoUpdateHdrSettingsRespStruct` |
| 画质 | `lyra` | `VideoUpdateHdrVividSettings` | `lyra::VideoUpdateHdrVividSettingsReqStruct` | `lyra::VideoUpdateHdrVividSettingsRespStruct` |
| 美颜/塑形 | `lyra` | `BeautyFaceApplyToAll` | `lyra::BeautyFaceApplyToAllReqStruct` | `lyra::BeautyFaceApplyToAllRespStruct` |
| 美颜/塑形 | `lyra` | `ConfigureEmbeddedAlgorithmTaskPersistence` | — | `lyra::ConfigureEmbeddedAlgorithmTaskPersistenceRespStruct` |
| 美颜/塑形 | `lyra` | `DeleteBeautyBodyPreset` | — | `lyra::DeleteBeautyBodyPresetRespStruct` |
| 美颜/塑形 | `lyra` | `DeleteBeautyFacePreset` | — | `lyra::DeleteBeautyFacePresetRespStruct` |
| 美颜/塑形 | `lyra` | `DeserializeBeautyBodyPreset` | — | `lyra::DeserializeBeautyBodyPresetRespStruct` |
| 美颜/塑形 | `lyra` | `DeserializeBeautyFacePreset` | — | `lyra::DeserializeBeautyFacePresetRespStruct` |
| 美颜/塑形 | `lyra` | `GetBeautyBodyPreset` | — | `lyra::GetBeautyBodyPresetRespStruct` |
| 美颜/塑形 | `lyra` | `GetBeautyFacePreset` | — | `lyra::GetBeautyFacePresetRespStruct` |
| 美颜/塑形 | `lyra` | `GetManualBeautyUndoRedoEnable` | — | `lyra::GetManualBeautyUndoRedoEnableRespStruct` |
| 美颜/塑形 | `lyra` | `GetRetouchManager` | — | `lyra::GetRetouchManagerRespStruct` |
| 美颜/塑形 | `lyra` | `RemoveAllFigure` | — | `lyra::RemoveAllFigureRespStruct` |
| 美颜/塑形 | `lyra` | `RemoveAutoBeautyBodyPreset` | — | `lyra::RemoveAutoBeautyBodyPresetRespStruct` |
| 美颜/塑形 | `lyra` | `RemoveAutoBeautyFacePreset` | — | `lyra::RemoveAutoBeautyFacePresetRespStruct` |
| 美颜/塑形 | `lyra` | `RemoveBeauty` | `lyra::RemoveBeautyReqStruct` | `lyra::RemoveBeautyRespStruct` |
| 美颜/塑形 | `lyra` | `RemoveBeautyFacePreset` | — | `lyra::RemoveBeautyFacePresetRespStruct` |
| 美颜/塑形 | `lyra` | `RemoveEmptyFigure` | `lyra::RemoveEmptyFigureReqStruct` | `lyra::RemoveEmptyFigureRespStruct` |
| 美颜/塑形 | `lyra` | `RemoveFigure` | `lyra::RemoveFigureReqStruct` | `lyra::RemoveFigureRespStruct` |
| 美颜/塑形 | `lyra` | `RemoveRetouchCover` | — | `lyra::RemoveRetouchCoverRespStruct` |
| 美颜/塑形 | `lyra` | `ResetManualBeautyEffect` | — | `lyra::ResetManualBeautyEffectRespStruct` |
| 美颜/塑形 | `lyra` | `SerializeBeautyBodyPreset` | — | `lyra::SerializeBeautyBodyPresetRespStruct` |
| 美颜/塑形 | `lyra` | `SerializeBeautyFacePreset` | — | `lyra::SerializeBeautyFacePresetRespStruct` |
| 美颜/塑形 | `lyra` | `SetAutoBeautyBodyPreset` | — | `lyra::SetAutoBeautyBodyPresetRespStruct` |
| 美颜/塑形 | `lyra` | `SetAutoBeautyFacePreset` | — | `lyra::SetAutoBeautyFacePresetRespStruct` |
| 美颜/塑形 | `lyra` | `SetBeauty` | `lyra::SetBeautyReqStruct` | `lyra::SetBeautyRespStruct` |
| 美颜/塑形 | `lyra` | `SetBeautyBodyPreset` | — | `lyra::SetBeautyBodyPresetRespStruct` |
| 美颜/塑形 | `lyra` | `SetBeautyFacePreset` | — | `lyra::SetBeautyFacePresetRespStruct` |
| 美颜/塑形 | `lyra` | `SetBeautyToAll` | `lyra::SetBeautyToAllReqStruct` | `lyra::SetBeautyToAllRespStruct` |
| 美颜/塑形 | `lyra` | `SetFigure` | `lyra::SetFigureReqStruct` | `lyra::SetFigureRespStruct` |
| 美颜/塑形 | `lyra` | `SetFigureToAll` | `lyra::SetFigureToAllReqStruct` | `lyra::SetFigureToAllRespStruct` |
| 美颜/塑形 | `lyra` | `SetHistoriesLimitConfig` | — | `lyra::SetHistoriesLimitConfigRespStruct` |
| 美颜/塑形 | `lyra` | `SetMakeupRoot` | `lyra::SetMakeupRootReqStruct` | `lyra::SetMakeupRootRespStruct` |
| 美颜/塑形 | `lyra` | `UpdateBeautyValue` | `lyra::UpdateBeautyValueReqStruct` | `lyra::UpdateBeautyValueRespStruct` |
| 美颜/塑形 | `lyra` | `UpdateManualBeautyBrush` | — | `lyra::UpdateManualBeautyBrushRespStruct` |
| 美颜/塑形 | `lyra` | `UpdateRetouchCover` | — | `lyra::UpdateRetouchCoverRespStruct` |
| 美颜/塑形 | `lyra` | `UpdateRetouchCoverStaticImage` | `lyra::UpdateRetouchCoverStaticImageReqStruct` | `lyra::UpdateRetouchCoverStaticImageRespStruct` |
| 美颜/塑形 | `lyra` | `WriteManualBeautyAlgCache` | — | `lyra::WriteManualBeautyAlgCacheRespStruct` |
| 跟踪/锁定 | `lyra` | `AddEditableMaterialKeyFrameTrackTarget` | — | `lyra::AddEditableMaterialKeyFrameTrackTargetRespStruct` |
| 跟踪/锁定 | `lyra` | `AddEditableMaterialObjectTrackTarget` | — | `lyra::AddEditableMaterialObjectTrackTargetRespStruct` |
| 跟踪/锁定 | `lyra` | `AddMaskTracking` | `lyra::AddMaskTrackingReqStruct` | `lyra::AddMaskTrackingRespStruct` |
| 跟踪/锁定 | `lyra` | `AddObjectLockedEffect` | — | `lyra::AddObjectLockedEffectRespStruct` |
| 跟踪/锁定 | `lyra` | `AddSingleSmartMotionKeyframes` | — | `lyra::AddSingleSmartMotionKeyframesRespStruct` |
| 跟踪/锁定 | `lyra` | `AddTempSmartMotionKeyframes` | — | `lyra::AddTempSmartMotionKeyframesRespStruct` |
| 跟踪/锁定 | `lyra` | `AddVideoObjectLocked` | `lyra::AddVideoObjectLockedReqStruct` | `lyra::AddVideoObjectLockedRespStruct` |
| 跟踪/锁定 | `lyra` | `AddVideoSmartMotion` | `lyra::AddVideoSmartMotionReqStruct` | `lyra::AddVideoSmartMotionRespStruct` |
| 跟踪/锁定 | `lyra` | `AddVideoTrackingListener` | — | `lyra::AddVideoTrackingListenerRespStruct` |
| 跟踪/锁定 | `lyra` | `AppendVideoObjectLocked` | `lyra::AppendVideoObjectLockedReqStruct` | `lyra::AppendVideoObjectLockedRespStruct` |
| 跟踪/锁定 | `lyra` | `ArrangeTimelineTracks` | — | `lyra::ArrangeTimelineTracksRespStruct` |
| 跟踪/锁定 | `lyra` | `BeginVideoTracking2` | — | `lyra::BeginVideoTracking2RespStruct` |
| 跟踪/锁定 | `lyra` | `CancelAutoCineMotionAlgorithm` | — | `lyra::CancelAutoCineMotionAlgorithmRespStruct` |
| 跟踪/锁定 | `lyra` | `CancelMotionBlur` | — | `lyra::CancelMotionBlurRespStruct` |
| 跟踪/锁定 | `lyra` | `CancelPreviewMotionBlur` | — | `lyra::CancelPreviewMotionBlurRespStruct` |
| 跟踪/锁定 | `lyra` | `CancelPreviewSlowMotion` | — | `lyra::CancelPreviewSlowMotionRespStruct` |
| 跟踪/锁定 | `lyra` | `CancelSlowMotion` | `lyra::CancelSlowMotionReqStruct` | `lyra::CancelSlowMotionRespStruct` |
| 跟踪/锁定 | `lyra` | `CancelVideoTracking` | — | `lyra::CancelVideoTrackingRespStruct` |
| 跟踪/锁定 | `lyra` | `CancelVideoTracking2` | — | `lyra::CancelVideoTracking2RespStruct` |
| 跟踪/锁定 | `lyra` | `CancelVideoTrackingV3` | `lyra::CancelVideoTrackingV3ReqStruct` | `lyra::CancelVideoTrackingV3RespStruct` |
| 跟踪/锁定 | `lyra` | `CleanupVideoTracking2` | — | `lyra::CleanupVideoTracking2RespStruct` |
| 跟踪/锁定 | `lyra` | `CopyVideoTrackingMap` | — | `lyra::CopyVideoTrackingMapRespStruct` |
| 跟踪/锁定 | `lyra` | `CropTrackTimeInterval` | — | `lyra::CropTrackTimeIntervalRespStruct` |
| 跟踪/锁定 | `lyra` | `CutTrackFragment` | — | `lyra::CutTrackFragmentRespStruct` |
| 跟踪/锁定 | `lyra` | `DeleteEditableMaterialKeyFrameTrackTarget` | — | `lyra::DeleteEditableMaterialKeyFrameTrackTargetRespStruct` |
| 跟踪/锁定 | `lyra` | `DeleteEditableMaterialTrack` | — | `lyra::DeleteEditableMaterialTrackRespStruct` |
| 跟踪/锁定 | `lyra` | `DestroyAutoCineMotionAlgorithm` | — | `lyra::DestroyAutoCineMotionAlgorithmRespStruct` |
| 跟踪/锁定 | `lyra` | `DrawObjectLockedFrame` | — | `lyra::DrawObjectLockedFrameRespStruct` |
| 跟踪/锁定 | `lyra` | `FindTrackingSegmentsByTrackedSegment` | — | `lyra::FindTrackingSegmentsByTrackedSegmentRespStruct` |
| 跟踪/锁定 | `lyra` | `FinishedTrackAction` | `lyra::FinishedTrackActionReqStruct` | `lyra::FinishedTrackActionRespStruct` |
| 跟踪/锁定 | `lyra` | `FixSegmentOverlapInTrack` | — | `lyra::FixSegmentOverlapInTrackRespStruct` |
| 跟踪/锁定 | `lyra` | `GetEditableMaterialTrackIntelligentType` | — | `lyra::GetEditableMaterialTrackIntelligentTypeRespStruct` |
| 跟踪/锁定 | `lyra` | `GetMotionBlurPath` | — | `lyra::GetMotionBlurPathRespStruct` |
| 跟踪/锁定 | `lyra` | `GetSingleTrackProcessedImage` | — | `lyra::GetSingleTrackProcessedImageRespStruct` |
| 跟踪/锁定 | `lyra` | `GetSlowMotionPath` | — | `lyra::GetSlowMotionPathRespStruct` |
| 跟踪/锁定 | `lyra` | `GetTrackPixelColor` | — | `lyra::GetTrackPixelColorRespStruct` |
| 跟踪/锁定 | `lyra` | `GetTrackerKeyPointTimeStamp` | — | `lyra::GetTrackerKeyPointTimeStampRespStruct` |
| 跟踪/锁定 | `lyra` | `GetTrackerPosition` | — | `lyra::GetTrackerPositionRespStruct` |
| 跟踪/锁定 | `lyra` | `GetTrackingBaseLineTrs` | — | `lyra::GetTrackingBaseLineTrsRespStruct` |
| 跟踪/锁定 | `lyra` | `GetTrackingTarget` | — | `lyra::GetTrackingTargetRespStruct` |
| 跟踪/锁定 | `lyra` | `GetVideoTrackingTargetSegment` | `lyra::GetVideoTrackingTargetSegmentReqStruct` | `lyra::GetVideoTrackingTargetSegmentRespStruct` |
| 跟踪/锁定 | `lyra` | `HasKeyframeTracking` | — | `lyra::HasKeyframeTrackingRespStruct` |
| 跟踪/锁定 | `lyra` | `IsLyricEffectNeedMotionBlur` | `lyra::IsLyricEffectNeedMotionBlurReqStruct` | `lyra::IsLyricEffectNeedMotionBlurRespStruct` |
| 跟踪/锁定 | `lyra` | `KeyframeTracking` | — | `lyra::KeyframeTrackingRespStruct` |
| 跟踪/锁定 | `lyra` | `MixedTrackMode` | — | `lyra::MixedTrackModeRespStruct` |
| 跟踪/锁定 | `lyra` | `MoveTrack` | — | `lyra::MoveTrackRespStruct` |
| 跟踪/锁定 | `lyra` | `MultiTrackModeMoveSegments` | `lyra::MultiTrackModeMoveSegmentsReqStruct` | `lyra::MultiTrackModeMoveSegmentsRespStruct` |
| 跟踪/锁定 | `lyra` | `MultiTrackModePasteSegments` | `lyra::MultiTrackModePasteSegmentsReqStruct` | `lyra::MultiTrackModePasteSegmentsRespStruct` |
| 跟踪/锁定 | `lyra` | `MultiTrackV2TDraftPreprocess` | `lyra::MultiTrackV2TDraftPreprocessReqStruct` | `lyra::MultiTrackV2TDraftPreprocessRespStruct` |
| 跟踪/锁定 | `lyra` | `MuteAllTracks` | — | `lyra::MuteAllTracksRespStruct` |
| 跟踪/锁定 | `lyra` | `NotifySlowMotionComplete` | — | `lyra::NotifySlowMotionCompleteRespStruct` |
| 跟踪/锁定 | `lyra` | `PauseAutoCineMotion` | — | `lyra::PauseAutoCineMotionRespStruct` |
| 跟踪/锁定 | `lyra` | `PauseMotionBlur` | — | `lyra::PauseMotionBlurRespStruct` |
| 跟踪/锁定 | `lyra` | `PreviewMotionBlur` | — | `lyra::PreviewMotionBlurRespStruct` |
| 跟踪/锁定 | `lyra` | `PreviewSlowMotionFrameBlending` | — | `lyra::PreviewSlowMotionFrameBlendingRespStruct` |
| 跟踪/锁定 | `lyra` | `PreviewSlowMotionOpticalFlow` | — | `lyra::PreviewSlowMotionOpticalFlowRespStruct` |
| 跟踪/锁定 | `lyra` | `QueryLyricEffectMotionBlurStatus` | — | `lyra::QueryLyricEffectMotionBlurStatusRespStruct` |
| 跟踪/锁定 | `lyra` | `RemoveEmptyTrack` | — | `lyra::RemoveEmptyTrackRespStruct` |
| 跟踪/锁定 | `lyra` | `RemoveTempSmartMotionKeyframes` | — | `lyra::RemoveTempSmartMotionKeyframesRespStruct` |
| 跟踪/锁定 | `lyra` | `RemoveVideoObjectLocked` | `lyra::RemoveVideoObjectLockedReqStruct` | `lyra::RemoveVideoObjectLockedRespStruct` |
| 跟踪/锁定 | `lyra` | `RemoveVideoSmartMotion` | `lyra::RemoveVideoSmartMotionReqStruct` | `lyra::RemoveVideoSmartMotionRespStruct` |
| 跟踪/锁定 | `lyra` | `RemoveVideoTracking` | `lyra::RemoveVideoTrackingReqStruct` | `lyra::RemoveVideoTrackingRespStruct` |
| 跟踪/锁定 | `lyra` | `RemoveVideoTrackingListener` | — | `lyra::RemoveVideoTrackingListenerRespStruct` |
| 跟踪/锁定 | `lyra` | `RenderIndexTrackMode` | `lyra::RenderIndexTrackModeReqStruct` | `lyra::RenderIndexTrackModeRespStruct` |
| 跟踪/锁定 | `lyra` | `RenderIndexTrackModeOn` | — | `lyra::RenderIndexTrackModeOnRespStruct` |
| 跟踪/锁定 | `lyra` | `ReplaceMainTrackSegment` | — | `lyra::ReplaceMainTrackSegmentRespStruct` |
| 跟踪/锁定 | `lyra` | `ResumeMotionBlur` | — | `lyra::ResumeMotionBlurRespStruct` |
| 跟踪/锁定 | `lyra` | `RunAutoCineMotionAlgorithm` | — | `lyra::RunAutoCineMotionAlgorithmRespStruct` |
| 跟踪/锁定 | `lyra` | `SaveAttachmentWorkflowTrackerInfo` | — | `lyra::SaveAttachmentWorkflowTrackerInfoRespStruct` |
| 跟踪/锁定 | `lyra` | `SaveVideoTracking2Data` | `lyra::SaveVideoTracking2DataReqStruct` | `lyra::SaveVideoTracking2DataRespStruct` |
| 跟踪/锁定 | `lyra` | `SetAudioTrackIndex` | `lyra::SetAudioTrackIndexReqStruct` | `lyra::SetAudioTrackIndexRespStruct` |
| 跟踪/锁定 | `lyra` | `SetFixClashInSameTrack` | — | `lyra::SetFixClashInSameTrackRespStruct` |
| 跟踪/锁定 | `lyra` | `SetIsOnlyOneSubtitleTrack` | — | `lyra::SetIsOnlyOneSubtitleTrackRespStruct` |
| 跟踪/锁定 | `lyra` | `SetMainTrackAdsorb` | `lyra::SetMainTrackAdsorbReqStruct` | `lyra::SetMainTrackAdsorbRespStruct` |
| 跟踪/锁定 | `lyra` | `SetMultiViewSeqChoseTrackId` | — | `lyra::SetMultiViewSeqChoseTrackIdRespStruct` |
| 跟踪/锁定 | `lyra` | `SetTrackAttributes` | `lyra::SetTrackAttributesReqStruct` | `lyra::SetTrackAttributesRespStruct` |
| 跟踪/锁定 | `lyra` | `SetTrackInfo` | — | `lyra::SetTrackInfoRespStruct` |
| 跟踪/锁定 | `lyra` | `SetTrackName` | `lyra::SetTrackNameReqStruct` | `lyra::SetTrackNameRespStruct` |
| 跟踪/锁定 | `lyra` | `SetTrackerSelectArea` | — | `lyra::SetTrackerSelectAreaRespStruct` |
| 跟踪/锁定 | `lyra` | `SetTrackingRelationCacheUpdateCallback` | — | `lyra::SetTrackingRelationCacheUpdateCallbackRespStruct` |
| 跟踪/锁定 | `lyra` | `SetVideoSmartMotionRunningMode` | `lyra::SetVideoSmartMotionRunningModeReqStruct` | `lyra::SetVideoSmartMotionRunningModeRespStruct` |
| 跟踪/锁定 | `lyra` | `SetVideoTrackingCallback2` | — | `lyra::SetVideoTrackingCallback2RespStruct` |
| 跟踪/锁定 | `lyra` | `SetVideoTrackingDataReadCallback2` | — | `lyra::SetVideoTrackingDataReadCallback2RespStruct` |
| 跟踪/锁定 | `lyra` | `SingleKeyframeTracking` | — | `lyra::SingleKeyframeTrackingRespStruct` |
| 跟踪/锁定 | `lyra` | `SplitScreenAddPlaceholderTrack` | — | `lyra::SplitScreenAddPlaceholderTrackRespStruct` |
| 跟踪/锁定 | `lyra` | `SplitScreenUpdateTrackerInfo` | — | `lyra::SplitScreenUpdateTrackerInfoRespStruct` |
| 跟踪/锁定 | `lyra` | `StartConvertMotionBlur` | — | `lyra::StartConvertMotionBlurRespStruct` |
| 跟踪/锁定 | `lyra` | `StartConvertSlowMotion` | `lyra::StartConvertSlowMotionReqStruct` | `lyra::StartConvertSlowMotionRespStruct` |
| 跟踪/锁定 | `lyra` | `StartLyricEffectMotionBlur` | `lyra::StartLyricEffectMotionBlurReqStruct` | `lyra::StartLyricEffectMotionBlurRespStruct` |
| 跟踪/锁定 | `lyra` | `StartVideoTracking` | — | `lyra::StartVideoTrackingRespStruct` |
| 跟踪/锁定 | `lyra` | `StartVideoTrackingV3` | `lyra::StartVideoTrackingV3ReqStruct` | `lyra::StartVideoTrackingV3RespStruct` |
| 跟踪/锁定 | `lyra` | `TrackViewSeek` | — | `lyra::TrackViewSeekRespStruct` |
| 跟踪/锁定 | `lyra` | `UpdateAdjustColorMaskTrackViewVisible` | — | `lyra::UpdateAdjustColorMaskTrackViewVisibleRespStruct` |
| 跟踪/锁定 | `lyra` | `UpdateLyricEffectMotionBlurPath` | `lyra::UpdateLyricEffectMotionBlurPathReqStruct` | `lyra::UpdateLyricEffectMotionBlurPathRespStruct` |
| 跟踪/锁定 | `lyra` | `UpdateVideoObjectLocked` | `lyra::UpdateVideoObjectLockedReqStruct` | `lyra::UpdateVideoObjectLockedRespStruct` |
| 跟踪/锁定 | `lyra` | `UpdateVideoObjectLockedEnable` | `lyra::UpdateVideoObjectLockedEnableReqStruct` | `lyra::UpdateVideoObjectLockedEnableRespStruct` |
| 跟踪/锁定 | `lyra` | `UpdateVideoSmartMotion` | `lyra::UpdateVideoSmartMotionReqStruct` | `lyra::UpdateVideoSmartMotionRespStruct` |
| 跟踪/锁定 | `lyra` | `UpdateVideoSmartMotionEnable` | `lyra::UpdateVideoSmartMotionEnableReqStruct` | `lyra::UpdateVideoSmartMotionEnableRespStruct` |
| 跟踪/锁定 | `lyra` | `UpdateVideoTracking2` | `lyra::UpdateVideoTracking2ReqStruct` | `lyra::UpdateVideoTracking2RespStruct` |
| 跟踪/锁定 | `lyra` | `VideoTracking` | `lyra::VideoTrackingReqStruct` | `lyra::VideoTrackingRespStruct` |
| 音频 AI | `lyra` | `AddAudioBeat` | `lyra::AddAudioBeatReqStruct` | `lyra::AddAudioBeatRespStruct` |
| 音频 AI | `lyra` | `AddLyricEffect` | `lyra::AddLyricEffectReqStruct` | `lyra::AddLyricEffectRespStruct` |
| 音频 AI | `lyra` | `AddTtsPart` | — | `lyra::AddTtsPartRespStruct` |
| 音频 AI | `lyra` | `AddVideoBeat` | `lyra::AddVideoBeatReqStruct` | `lyra::AddVideoBeatRespStruct` |
| 音频 AI | `lyra` | `AudioChangeVoice` | `lyra::AudioChangeVoiceReqStruct` | `lyra::AudioChangeVoiceRespStruct` |
| 音频 AI | `lyra` | `AudioChangeVoiceAdjust` | `lyra::AudioChangeVoiceAdjustReqStruct` | `lyra::AudioChangeVoiceAdjustRespStruct` |
| 音频 AI | `lyra` | `AudioLoudness` | `lyra::AudioLoudnessReqStruct` | `lyra::AudioLoudnessRespStruct` |
| 音频 AI | `lyra` | `AudioLoudnessUnify` | — | `lyra::AudioLoudnessUnifyRespStruct` |
| 音频 AI | `lyra` | `AudioSeparateSound` | `lyra::AudioSeparateSoundReqStruct` | `lyra::AudioSeparateSoundRespStruct` |
| 音频 AI | `lyra` | `BatchMoveSuccessorTts` | — | `lyra::BatchMoveSuccessorTtsRespStruct` |
| 音频 AI | `lyra` | `CancelLyricEffect` | `lyra::CancelLyricEffectReqStruct` | `lyra::CancelLyricEffectRespStruct` |
| 音频 AI | `lyra` | `CanvasRemoveRadiusCornerBorder` | — | `lyra::CanvasRemoveRadiusCornerBorderRespStruct` |
| 音频 AI | `lyra` | `CanvasRemoveTransform` | — | `lyra::CanvasRemoveTransformRespStruct` |
| 音频 AI | `lyra` | `ChangeVoiceApplyToAll` | `lyra::ChangeVoiceApplyToAllReqStruct` | `lyra::ChangeVoiceApplyToAllRespStruct` |
| 音频 AI | `lyra` | `ClearDraftLyricEffect` | — | `lyra::ClearDraftLyricEffectRespStruct` |
| 音频 AI | `lyra` | `ClearLyricEffectBySource` | `lyra::ClearLyricEffectBySourceReqStruct` | `lyra::ClearLyricEffectBySourceRespStruct` |
| 音频 AI | `lyra` | `DetectAudioLoudness` | `lyra::DetectAudioLoudnessReqStruct` | `lyra::DetectAudioLoudnessRespStruct` |
| 音频 AI | `lyra` | `DetectVoiceActivity` | — | `lyra::DetectVoiceActivityRespStruct` |
| 音频 AI | `lyra` | `DigitalHumanConvertTts` | — | `lyra::DigitalHumanConvertTtsRespStruct` |
| 音频 AI | `lyra` | `EnableVocalBeautify` | `lyra::EnableVocalBeautifyReqStruct` | `lyra::EnableVocalBeautifyRespStruct` |
| 音频 AI | `lyra` | `EnableVocalBeautifyWithParam` | `lyra::EnableVocalBeautifyWithParamReqStruct` | `lyra::EnableVocalBeautifyWithParamRespStruct` |
| 音频 AI | `lyra` | `GenerateCurveSpeedPointsFromBeats` | — | `lyra::GenerateCurveSpeedPointsFromBeatsRespStruct` |
| 音频 AI | `lyra` | `GetAllAudioBeats` | — | `lyra::GetAllAudioBeatsRespStruct` |
| 音频 AI | `lyra` | `GetAllBeats` | — | `lyra::GetAllBeatsRespStruct` |
| 音频 AI | `lyra` | `GetAllVideoBeats` | — | `lyra::GetAllVideoBeatsRespStruct` |
| 音频 AI | `lyra` | `GetLyricEffectCombinationSegmentId` | `lyra::GetLyricEffectCombinationSegmentIdReqStruct` | `lyra::GetLyricEffectCombinationSegmentIdRespStruct` |
| 音频 AI | `lyra` | `GetLyricsRecognizeInfo` | `lyra::GetLyricsRecognizeInfoReqStruct` | `lyra::GetLyricsRecognizeInfoRespStruct` |
| 音频 AI | `lyra` | `GetRequestTtsParams` | — | `lyra::GetRequestTtsParamsRespStruct` |
| 音频 AI | `lyra` | `GetResourcesFromLyricsEffect` | `lyra::GetResourcesFromLyricsEffectReqStruct` | `lyra::GetResourcesFromLyricsEffectRespStruct` |
| 音频 AI | `lyra` | `GetVocalSeparationPath` | — | `lyra::GetVocalSeparationPathRespStruct` |
| 音频 AI | `lyra` | `GetVoiceType` | — | `lyra::GetVoiceTypeRespStruct` |
| 音频 AI | `lyra` | `MediaToneModify` | `lyra::MediaToneModifyReqStruct` | `lyra::MediaToneModifyRespStruct` |
| 音频 AI | `lyra` | `OnlyExportNeedRecognitionFragments` | — | `lyra::OnlyExportNeedRecognitionFragmentsRespStruct` |
| 音频 AI | `lyra` | `RegisterLyricEffectDowngradeCallback` | — | `lyra::RegisterLyricEffectDowngradeCallbackRespStruct` |
| 音频 AI | `lyra` | `RemoveAudioBeat` | `lyra::RemoveAudioBeatReqStruct` | `lyra::RemoveAudioBeatRespStruct` |
| 音频 AI | `lyra` | `RemoveAudioChangeVoice` | `lyra::RemoveAudioChangeVoiceReqStruct` | `lyra::RemoveAudioChangeVoiceRespStruct` |
| 音频 AI | `lyra` | `RemoveAudioLoudness` | `lyra::RemoveAudioLoudnessReqStruct` | `lyra::RemoveAudioLoudnessRespStruct` |
| 音频 AI | `lyra` | `RemoveBeats` | — | `lyra::RemoveBeatsRespStruct` |
| 音频 AI | `lyra` | `RemoveLyricEffect` | — | `lyra::RemoveLyricEffectRespStruct` |
| 音频 AI | `lyra` | `RemoveLyricEffectGroup` | `lyra::RemoveLyricEffectGroupReqStruct` | `lyra::RemoveLyricEffectGroupRespStruct` |
| 音频 AI | `lyra` | `RemoveVideoBeat` | `lyra::RemoveVideoBeatReqStruct` | `lyra::RemoveVideoBeatRespStruct` |
| 音频 AI | `lyra` | `ResetVocalBeautify` | `lyra::ResetVocalBeautifyReqStruct` | `lyra::ResetVocalBeautifyRespStruct` |
| 音频 AI | `lyra` | `RevertBeatsFromAudio` | — | `lyra::RevertBeatsFromAudioRespStruct` |
| 音频 AI | `lyra` | `SeparateVideoAudio` | `lyra::SeparateVideoAudioReqStruct` | `lyra::SeparateVideoAudioRespStruct` |
| 音频 AI | `lyra` | `SetBeats` | — | `lyra::SetBeatsRespStruct` |
| 音频 AI | `lyra` | `SetDefaultTtsParamCallback` | — | `lyra::SetDefaultTtsParamCallbackRespStruct` |
| 音频 AI | `lyra` | `SetLyricsAdaptMusic` | — | `lyra::SetLyricsAdaptMusicRespStruct` |
| 音频 AI | `lyra` | `SetVocalBeautifyAmbientSoundLevel` | `lyra::SetVocalBeautifyAmbientSoundLevelReqStruct` | `lyra::SetVocalBeautifyAmbientSoundLevelRespStruct` |
| 音频 AI | `lyra` | `SetVocalBeautifyProductionPath` | `lyra::SetVocalBeautifyProductionPathReqStruct` | `lyra::SetVocalBeautifyProductionPathRespStruct` |
| 音频 AI | `lyra` | `SetVocalBeautifySlideValue` | `lyra::SetVocalBeautifySlideValueReqStruct` | `lyra::SetVocalBeautifySlideValueRespStruct` |
| 音频 AI | `lyra` | `SetVocalBeautifyVoiceChangeMode` | `lyra::SetVocalBeautifyVoiceChangeModeReqStruct` | `lyra::SetVocalBeautifyVoiceChangeModeRespStruct` |
| 音频 AI | `lyra` | `TemplateRemoveBeats` | `lyra::TemplateRemoveBeatsReqStruct` | `lyra::TemplateRemoveBeatsRespStruct` |
| 音频 AI | `lyra` | `TemplateResetVoiceSeparate` | — | `lyra::TemplateResetVoiceSeparateRespStruct` |
| 音频 AI | `lyra` | `TemplateSetBeats` | `lyra::TemplateSetBeatsReqStruct` | `lyra::TemplateSetBeatsRespStruct` |
| 音频 AI | `lyra` | `TtsBatchUpdateVoice` | — | `lyra::TtsBatchUpdateVoiceRespStruct` |
| 音频 AI | `lyra` | `TtsUpdate` | — | `lyra::TtsUpdateRespStruct` |
| 音频 AI | `lyra` | `UpdateAudioLoudness` | `lyra::UpdateAudioLoudnessReqStruct` | `lyra::UpdateAudioLoudnessRespStruct` |
| 音频 AI | `lyra` | `UpdateLyricTemplate` | `lyra::UpdateLyricTemplateReqStruct` | `lyra::UpdateLyricTemplateRespStruct` |
| 音频 AI | `lyra` | `UpdateMutableMaterialLyric` | — | `lyra::UpdateMutableMaterialLyricRespStruct` |
| 音频 AI | `lyra` | `UpdateScriptVideoTtsAllPart` | — | `lyra::UpdateScriptVideoTtsAllPartRespStruct` |
| 音频 AI | `lyra` | `UpdateScriptVideoTtsPart` | — | `lyra::UpdateScriptVideoTtsPartRespStruct` |
| 音频 AI | `lyra` | `UpdateSegmentsAudioPitchShiftSwitch` | — | `lyra::UpdateSegmentsAudioPitchShiftSwitchRespStruct` |
| 音频 AI | `lyra` | `UpdateSegmentsAudioPitchShiftValue` | — | `lyra::UpdateSegmentsAudioPitchShiftValueRespStruct` |
| 音频 AI | `lyra` | `UpdateSpeakerTtsInfo` | — | `lyra::UpdateSpeakerTtsInfoRespStruct` |
| 音频 AI | `lyra` | `UpdateTextToAudioTone` | `lyra::UpdateTextToAudioToneReqStruct` | `lyra::UpdateTextToAudioToneRespStruct` |
| 音频 AI | `lyra` | `UpdateVocalSeparationChoice` | `lyra::UpdateVocalSeparationChoiceReqStruct` | `lyra::UpdateVocalSeparationChoiceRespStruct` |
| 音频 AI | `lyra` | `VideoLoudnessUnify` | `lyra::VideoLoudnessUnifyReqStruct` | `lyra::VideoLoudnessUnifyRespStruct` |
| 音频 AI | `lyra` | `VoTtsChangeSpeed` | — | `lyra::VoTtsChangeSpeedRespStruct` |

## 二、AI 流水线目录（源码树还原）

| 文件数 | 目录 | 样本文件 |
| ---: | --- | --- |
| 86 | `lyra/generated/attachment/model` | `attachment_ai_asset_info.cpp`<br>`attachment_ai_chat_sugs_info.cpp`<br>`attachment_ai_clipper_info.cpp`<br>`attachment_ai_clipper_transcript.cpp`<br>`attachment_ai_clipper_transcript_chapter.cpp` |
| 54 | `lyra/generated/draft` | `ai_background.cpp`<br>`ai_beats.cpp`<br>`ai_emoji_config.cpp`<br>`ai_generate_task_info.cpp`<br>`ai_in_painting.cpp` |
| 15 | `lyra/trash_src/migration/tasks` | `migration_to_1060000.cpp`<br>`migration_to_1160001.cpp`<br>`migration_to_1250000.cpp`<br>`migration_to_1260000.cpp`<br>`migration_to_1270000.cpp` |
| 11 | `lyra/service/patch/helper/patch_extra_handlers/algorithm` | `ai_matting_handler.cpp`<br>`algorithm_crypto_helper.cpp`<br>`custom_matting_handler.cpp`<br>`denoise_handler.cpp`<br>`frame_interpolation_handler.cpp` |
| 11 | `lyra/ve_wrapper/clipflow/shell/common_node` | `aigc_effect_start_ve_task_mix_node.cpp`<br>`batch_remote_task_node.cpp`<br>`clip_audio_node.cpp`<br>`clip_video_node.cpp`<br>`copy_node.cpp` |
| 9 | `lyra/trash_platform/pubapi` | `ai_beat_manager.cpp`<br>`ai_matting_client_pubapi.cpp`<br>`mask_tracking_service.cpp`<br>`matting_task_service.cpp`<br>`media_algorithm.cpp` |
| 9 | `lyra/ve_wrapper/algorithm` | `algorithm_cache_wrapper.cpp`<br>`algorithm_cache_wrapper_impl_v1.cpp`<br>`algorithm_cache_wrapper_impl_v2.cpp`<br>`algorithm_cache_wrapper_utils.cpp`<br>`algorithm_engine.cpp` |
| 8 | `lyra/service/draft/repair/tasks` | `draft_duration_repair_task.cpp`<br>`main_track_duplicate_repair_task.cpp`<br>`material_duration_repair_task.cpp`<br>`render_index_conflict_repair_task.cpp`<br>`seg_id_confict_repair_task.cpp` |
| 8 | `lyra/ve_wrapper/algorithm/utils` | `algorithm_async_utils.cpp`<br>`algorithm_cache_manager.cpp`<br>`algorithm_cache_persistence.cpp`<br>`algorithm_compiler.cpp`<br>`algorithm_overlay_helper.cpp` |
| 8 | `lyra/ve_wrapper/clipflow/task/material_generation/node` | `build_item_node.cpp`<br>`check_gen_status_node.cpp`<br>`extract_frames_node.cpp`<br>`image_parse_node.cpp`<br>`image_parse_node_prod.cpp` |
| 7 | `lyra/ve_wrapper/clipflow/task/subtitle_recognize/node` | `detach_audio_node.cpp`<br>`poll_asr_result_node.cpp`<br>`submit_asr_node.cpp`<br>`subtitle_recognize_node_utils.cpp`<br>`talking_head_cleanup_node.cpp` |
| 3 | `lyra/service/ai_edit/rough_edit` | `ai_clipper_transcript_edit_helper.cpp`<br>`roughcut2_edit_imp.cpp`<br>`roughcut_edit_imp.cpp` |
| 3 | `lyra/service/async_task/manager/json_obj` | `asynctasknew.cpp`<br>`asynctaskpush.cpp`<br>`asynctaskquery.cpp` |
| 3 | `lyra/service/async_task/manager/request_group` | `async_task_request_group.cpp`<br>`async_task_request_group_item.h`<br>`async_task_request_group_manager.cpp` |
| 3 | `lyra/service/tail_leader` | `tail_leader_default_impl.cpp`<br>`tail_leader_driver_impl.cpp`<br>`tail_leader_service.cpp` |
| 3 | `lyra/ve_wrapper/clipflow/task/publish_inspriation/node` | `inspiration_publish_init_node.cpp`<br>`inspiration_publish_node.cpp`<br>`inspiration_publish_upload_node.cpp` |
| 2 | `lyra/base/looper/thread_looper` | `task_executor.h`<br>`task_executor_impl.h` |
| 2 | `lyra/base/lb_thread` | `priority_task_executor.cpp`<br>`priority_task_executor_impl.h` |
| 2 | `lyra/base/looper/main_looper/platform/win` | `message_loop_win.cpp`<br>`message_window_win.cpp` |
| 2 | `lyra/generated/action/params` | `recognized_subtitle_word_param.cpp`<br>`single_face_adjust_param.cpp` |
| 2 | `lyra/service/text/helper` | `ai_generate_text_utils.h`<br>`ai_text_effect_utils.h` |
| 2 | `lyra/service/ai_edit/common` | `ai_edit_base_utils.cpp`<br>`clipinfo_protocol_result.cpp` |
| 2 | `lyra/service/ai_edit/script_ai_cut` | `ai_edit_script_utils.cpp`<br>`script_ai_cut_impl.cpp` |
| 2 | `lyra/service/ai_moment` | `ai_moment_action_impl.cpp`<br>`ai_moment_service.cpp` |
| 2 | `lyra/service/aigc_generate` | `aigc_generate_impl.cpp`<br>`aigc_generate_service.cpp` |
| 2 | `lyra/service/aigc_workflow` | `aigc_workflow_action_impl.cpp`<br>`aigc_workflow_service.cpp` |
| 2 | `lyra/service/algorithm` | `algorithm_impl.cpp`<br>`algorithm_service.cpp` |
| 2 | `lyra/service/async_task/manager/merge_group` | `async_task_merge_group.cpp`<br>`async_task_merge_group_manager.cpp` |
| 2 | `lyra/service/audio/helper` | `audio_algorithm_utils.cpp`<br>`voice_activity_detection_manager.cpp` |
| 2 | `lyra/service/bach_algorithm_cache` | `bach_algorithm_cache_impl.cpp`<br>`bach_algorithm_cache_service.cpp` |
| 2 | `lyra/service/draft/repair` | `draft_repair_engine.cpp`<br>`draft_repair_pipeline_controller.cpp` |
| 2 | `lyra/service/patch/helper/cli_intent/face_beauty` | `face_beauty_cli_intent_handler.cpp`<br>`face_beauty_cli_intent_resolver.cpp` |
| 2 | `lyra/service/smart_crop` | `smart_crop_default_impl.cpp`<br>`smart_crop_service.cpp` |
| 2 | `lyra/service/smart_edit` | `smart_edit_action_impl.cpp`<br>`smart_edit_service.cpp` |
| 2 | `lyra/service/smart_relight/keyframe` | `set_light_source_keyframe.cpp`<br>`set_light_source_keyframe.h` |
| 2 | `lyra/service/smart_relight` | `smart_relight_default_impl.cpp`<br>`smart_relight_service.cpp` |
| 2 | `lyra/service/video_algorithm` | `video_algorithm_default_impl.cpp`<br>`video_algorithm_service.cpp` |
| 2 | `lyra/trash_src/attachment/ai_clipper` | `attachment_ai_clipper_control.cpp`<br>`attachment_ai_clipper_transcript_control.cpp` |
| 2 | `lyra/trash_src/business/materials/preset` | `preset_beauty_body.cpp`<br>`preset_beauty_face.cpp` |
| 2 | `lyra/trash_src/draft_cross/template/json_parser` | `ai_text_template_path_corrector.cpp`<br>`template_beauty_path_corrector.cpp` |

## 三、端侧模型包规格

| 目录 | 域 | MB | 文件数 | 权重文件 | 规格文件 |
| --- | --- | ---: | ---: | --- | --- |
| `media_search` | 其它 | 31.58 | 8 | `ptl_2.dat` 31.0MB<br>`ptl_1.dat` 0.56MB<br>`ptl_2.idx` 0.01MB<br>`ptl_1.idx` 0.01MB | — |
| `audiomodel` | 其它 | 31.07 | 8 | `aed40_10m.model` 9.33MB<br>`sentence_score_v1.0.model` 6.04MB<br>`music2vibes_video_mobile_v1.0.model` 4.84MB<br>`aed_pets_v3.0.model` 4.76MB | — |
| `freidmodel` | 人脸 | 23.63 | 3 | `tt_freid_v2.0.model` 11.82MB<br>`tt_freid_v1.0.model` 5.91MB<br>`qingyan_freid_v1.0.model` 5.91MB | — |
| `tt_mobilevos` | 其它 | 22.34 | 2 | `mobilevos_packed_v1.1.model` 11.19MB<br>`mobilevos_v1.1.model` 11.15MB | — |
| `mattingmodel` | 抠像/分割 | 20.03 | 7 | `saliency_matting_v1.0.model` 6.74MB<br>`tt_matting_video_v1.0.model` 5.64MB<br>`video_saliency_seg_bce_v1.0.model` 3.79MB<br>`tt_matting_video_gru_v1.0.model` 3.44MB | — |
| `tt_interactive_matting` | 抠像/分割 | 10.53 | 1 | `tt_interactive_matting_v1.0.model` 10.53MB | — |
| `interpolation` | 画质 | 10.05 | 1 | `lens_vfi_v1.0.model` 10.05MB | — |
| `avatar3d` | 数字人 | 10.04 | 1 | `tt_avatar3d_v4.0.model` 10.04MB | — |
| `alg_scene_normal` | 智能剪辑决策 | 5.14 | 1 | `bingo_scene_normal_tt_v2.1_size0.model` 5.14MB | — |
| `scene_normal_model` | 智能剪辑决策 | 5.14 | 1 | `bingo_scene_normal_v2.0.model` 5.14MB | — |
| `bingo_facegan_model` | 人脸 | 5.1 | 1 | `female_gan_v3.0.model` 5.1MB | — |
| `faceclustingmodel` | 人脸 | 4.7 | 2 | `douyin_leader_v1.0.model` 3.1MB<br>`tt_bigbrother_v6.0.model` 1.59MB | — |
| `tt_gendergan` | 人脸 | 4.34 | 1 | `tt_gendergan_v4.2.model` 4.34MB | — |
| `faceverifymodel` | 人脸 | 4.14 | 1 | `tt_faceverify_v7.0.model` 4.14MB | — |
| `saliency_seg_model` | 其它 | 3.65 | 1 | `bingo_saliency_seg_v1.0.model` 3.65MB | — |
| `mangamodel` | 其它 | 2.92 | 1 | `ap_manga_v1.0.model` 2.92MB | — |
| `tt_facefitting_3d` | 美颜/塑形 | 2.0 | 1 | `tt_facefitting_3d_v6.1.model` 2.0MB | — |
| `v2-models` | 其它 | 1.74 | 12 | `smartcodec_v1.nnet` 0.29MB<br>`smartcodec_v1.nnet` 0.29MB<br>`smartcodec_v1.nnet` 0.29MB<br>`smartcodec_v1.nnet` 0.29MB | — |
| `invisible_watermark` | 其它 | 1.53 | 2 | `win_lens_wm_embed_model_c4_v2.bytenn` 0.76MB<br>`mac_lens_wm_embed_model_c4_v2.bytenn` 0.76MB | — |
| `tt_salient_human` | 抠像/分割 | 1.39 | 1 | `tt_salient_human_v1.0.model` 1.39MB | — |
| `SegmentJS` | 其它 | 1.34 | 4 | `main.js` 0.73MB<br>`template.js` 0.61MB<br>`package_info.json` 0.0MB<br>`version.json` 0.0MB | — |
| `depthmodel` | 其它 | 1.15 | 1 | `tt_depth_estimation_v3.0.model` 1.15MB | — |
| `facefitting` | 美颜/塑形 | 1.15 | 2 | `tt_facefitting1256_v2.0.model` 0.63MB<br>`tt_facefitting1220_v2.0.model` 0.52MB | — |
| `aec` | 其它 | 1.14 | 2 | `aec44k_v1.2.model` 0.85MB<br>`aec44k_resnet_echo_cancellation_v1.2.model` 0.29MB | — |
| `v1-models` | 其它 | 1.05 | 8 | `smartcodec_v1.nnet` 0.28MB<br>`smartcodec_v1.nnet` 0.27MB<br>`smartcodec_v1.nnet` 0.27MB<br>`smartcodec_v1.nnet` 0.23MB | — |
| `petfacemodel` | 人脸 | 1.03 | 1 | `tt_petface_v5.2.model` 1.03MB | — |
| `idream` | AIGC 生成 | 0.93 | 1 | `tt_eyegrad_v1.0.model` 0.93MB | — |
| `humanparsingmodel` | 其它 | 0.73 | 1 | `tt_human_parsing_for_jianying_v1.0.model` 0.73MB | — |
| `skin_seg` | 其它 | 0.64 | 2 | `tt_skin_seg_video_seg_fp16_v1.0.model` 0.39MB<br>`tt_skin_seg_v5.0.model` 0.25MB | — |
| `avatar_drive` | 数字人 | 0.6 | 1 | `tt_avatar_drive_v1.0.model` 0.6MB | — |
| `handmodel` | 其它 | 0.6 | 3 | `tt_hand_kp_v6.0.model` 0.33MB<br>`tt_hand_gesture_v11.0.model` 0.21MB<br>`tt_hand_det_v11.0.model` 0.06MB | — |
| `facebeautifymodel` | 人脸 | 0.55 | 1 | `tt_facebeautify_v2.0.model` 0.55MB | — |
| `nh_nodehub_image` | 其它 | 0.44 | 1 | `nodehub_image_saliency_v1.0.model` 0.44MB | — |
| `skeleton_model` | 其它 | 0.38 | 1 | `tt_skeleton_v7.0.model` 0.38MB | — |
| `noise_reduction` | 其它 | 0.24 | 1 | `nn_denoise.bytenn` 0.24MB | — |
| `colorcard` | 其它 | 0.16 | 1 | `lookup.png` 0.16MB | — |
| `object_tracking` | 跟踪/锁定 | 0.16 | 1 | `bingo_objectTracking_v1.0.dat` 0.16MB | — |
| `tt_eyefitting` | 美颜/塑形 | 0.1 | 1 | `tt_eyefitting_v1.0.model` 0.1MB | — |
| `umvfi` | 画质 | 0.09 | 1 | `umvfi.metallib` 0.09MB | — |
| `deflicker` | 画质 | 0.08 | 1 | `deflicker.metallib` 0.08MB | — |
| `hairparser` | 其它 | 0.08 | 1 | `tt_hair_v11.0.model` 0.08MB | — |
| `headsegmodel` | 其它 | 0.04 | 1 | `tt_headseg_v6.0.model` 0.04MB | — |
| `nh_script` | 其它 | 0.03 | 1 | `saliencyseg_crop_script.model` 0.03MB | — |
| `oilpaintbrush` | 其它 | 0.02 | 1 | `brush1.png` 0.02MB | — |
| `jianying_aigc_charge` | AIGC 生成 | 0.0 | 1 | `jianying_aigc_charge_v1.0_size0.model` 0.0MB | — |

## 四、云 API 服务目录

| 服务/动作 | 出现模块 |
| --- | --- |
| `account/get_pippit_token` | agent_runtime_addon.node |
| `account/get_pippit_user_info` | agent_runtime_addon.node |
| `account/user` | DeepAgentsService.dll |
| `ai_writing/get_results_by_images` | agent_runtime_addon.node |
| `ai_writing/get_results_by_texts` | agent_runtime_addon.node |
| `aigc_image/super_resolution` | DeepAgentsService.dll |
| `aigc_text/get_voiceclone_text` | DeepAgentsService.dll |
| `asset/create_cloud_asset` | agent_runtime_addon.node |
| `asset/detail` | DeepAgentsService.dll |
| `asset/prepare_upload_cloud` | agent_runtime_addon.node |
| `audio_subtitle/feedback` | DeepAgentsService.dll |
| `audio_subtitle/get_keyword` | DeepAgentsService.dll |
| `audio_subtitle/highlight` | videoeditor.dll |
| `audio_subtitle/query` | DeepAgentsService.dll |
| `audio_subtitle/submit` | DeepAgentsService.dll |
| `audio_subtitle/update_keyword` | DeepAgentsService.dll |
| `benefit_redemption` | DeepAgentsService.dll |
| `calc_video_score` | DeepAgentsService.dll |
| `capflow/cancel` | DeepAgentsService.dll |
| `capflow/history_task` | DeepAgentsService.dll |
| `capflow/query` | DeepAgentsService.dll |
| `capflow/submit` | DeepAgentsService.dll |
| `check_rate_limit` | DeepAgentsService.dll |
| `check_spam` | DeepAgentsService.dll |
| `cloud/auto_upload` | agent_runtime_addon.node |
| `cloud/group` | agent_runtime_addon.node |
| `cloud/upload` | agent_runtime_addon.node |
| `cloud_property/get_user_recent_package` | agent_runtime_addon.node |
| `cloud_property/property_count` | agent_runtime_addon.node |
| `cloud_property/search` | agent_runtime_addon.node |
| `common_task/cancel` | videoeditor.dll |
| `common_task/new` | videoeditor.dll |
| `common_task/query` | videoeditor.dll |
| `common_task/sync` | videoeditor.dll |
| `coordination/batch_send_message` | agent_runtime_addon.node |
| `coordination/check_white_list` | DeepAgentsService.dll |
| `coordination/cluster_create` | DeepAgentsService.dll |
| `coordination/get_share_info` | agent_runtime_addon.node |
| `coordination/mark_notice` | DeepAgentsService.dll |
| `coordination/owner_share_list` | agent_runtime_addon.node |
| `coordination/record_delete` | agent_runtime_addon.node |
| `coordination/share_create` | agent_runtime_addon.node |
| `coordination/share_update` | agent_runtime_addon.node |
| `coordination/shared_record_list` | agent_runtime_addon.node |
| `copilot/conversation` | DeepAgentsService.dll |
| `copilot/get_preupload_time` | DeepAgentsService.dll |
| `copilot/modify_message` | DeepAgentsService.dll |
| `copilot/section` | DeepAgentsService.dll |
| `copilot/upload_material` | DeepAgentsService.dll |
| `custom_service/get_entrance` | DeepAgentsService.dll |
| `custom_service/get_entrance_allow_guest` | DeepAgentsService.dll |
| `custom_service/im` | agent_runtime_addon.node |
| `edit/get_config` | agent_runtime_addon.node |
| `effect/search` | resourcecli.dll |
| `encrypt/get_public_key` | videoeditor.dll |
| `ever_photo/get_token` | DeepAgentsService.dll |
| `ever_photo/promote_asset` | DeepAgentsService.dll |
| `font/check` | agent_runtime_addon.node |
| `get_collection_songs` | resourcecli.dll |
| `get_collections` | resourcecli.dll |
| `get_music_effect_collections` | resourcecli.dll |
| `get_my_douyin_songs` | resourcecli.dll |
| `get_my_tiktok_songs` | resourcecli.dll |
| `get_recommend_songs` | resourcecli.dll |
| `get_sami_token` | videoeditor.dll |
| `get_user_vid_list` | agent_runtime_addon.node |
| `group/templates` | agent_runtime_addon.node |
| `image/anime_copyright_checker` | agent_runtime_addon.node |
| `image/content_classifier` | agent_runtime_addon.node |
| `image/face_compare` | agent_runtime_addon.node |
| `intelligent_edit/security_audit` | agent_runtime_addon.node |
| `lan_transfer/get_user_devices_info` | agent_runtime_addon.node |
| `lan_transfer/upload_device_info` | agent_runtime_addon.node |
| `multi_get_songs` | resourcecli.dll |
| `music/filter` | resourcecli.dll |
| `music/get_recommend_music` | resourcecli.dll |
| `music/similar_music_rec` | resourcecli.dll |
| `music/template_music_recommend` | resourcecli.dll |
| `music_finger` | resourcecli.dll |
| `music_scene_check` | agent_runtime_addon.node |
| `notice/list` | agent_runtime_addon.node |
| `notice/unread_count` | agent_runtime_addon.node |
| `oauth/access_token` | DeepAgentsService.dll |
| `pc/aweme_collection_songs` | DeepAgentsService.dll |
| `pc/commerce_replicate` | agent_runtime_addon.node |
| `pc/export_page` | agent_runtime_addon.node |
| `pc/get_user_info` | DeepAgentsService.dll |
| `pc/get_user_keyboard_shortcut` | DeepAgentsService.dll |
| `pc/homepage` | DeepAgentsService.dll |
| `pc/replicate` | DeepAgentsService.dll |
| `pc/search` | DeepAgentsService.dll, agent_runtime_addon.node |
| `pc/share` | agent_runtime_addon.node |
| `pc/storyboard` | DeepAgentsService.dll |
| `pc/to_shoot` | DeepAgentsService.dll |
| `pc/update_user_keyboard_shortcut` | DeepAgentsService.dll |
| `pc/zenith` | DeepAgentsService.dll |
| `persona/get_features` | agent_runtime_addon.node |
| `personal/pc` | agent_runtime_addon.node |
| `purchase/purchase_templates` | DeepAgentsService.dll |
| `replicate/add` | agent_runtime_addon.node |
| `replicate/add_usage_amount` | agent_runtime_addon.node |
| `replicate/delete` | agent_runtime_addon.node |
| `replicate/get_collection_templates` | DeepAgentsService.dll |
| `replicate/get_collections` | DeepAgentsService.dll |
| `replicate/update_settings` | DeepAgentsService.dll |
| `report/report` | DeepAgentsService.dll |
| `search/songs` | resourcecli.dll |
| `search/sug_topic` | agent_runtime_addon.node |
| `search_songs` | resourcecli.dll |
| `smart_recognition` | agent_runtime_addon.node |
| `smartvideo/text_video` | agent_runtime_addon.node |
| `text_correction/get_correction_rlt` | DeepAgentsService.dll |
| `text_to_audio` | videoeditor.dll |
| `text_to_video/parse_article_url` | agent_runtime_addon.node |
| `text_to_video/prompt_to_text` | agent_runtime_addon.node |
| `text_to_video/query_generate_video_task` | agent_runtime_addon.node |
| `text_to_video/submit_generate_video_task` | agent_runtime_addon.node |
| `third_crawl` | resourcecli.dll |
| `third_resource/favorite` | agent_runtime_addon.node |
| `third_resource/get_category_info` | agent_runtime_addon.node |
| `third_resource/mget` | agent_runtime_addon.node |
| `third_resource/mget_by_category_id` | agent_runtime_addon.node |
| `third_resource/mget_favorite_info` | agent_runtime_addon.node |
| `third_resource/search` | agent_runtime_addon.node |
| `topic/get_topic_list` | agent_runtime_addon.node |
| `translate/translate_texts` | videoeditor.dll |
| `trial/batch_query_eligibility` | agent_runtime_addon.node |
| `trial/finished_report` | agent_runtime_addon.node |
| `update_user_vid_list` | agent_runtime_addon.node |
| `upload_sign` | DeepAgentsService.dll, agent_runtime_addon.node |
| `user/get_enable_list` | DeepAgentsService.dll |
| `user/oauth` | agent_runtime_addon.node |
| `user/update` | DeepAgentsService.dll |
| `vmtag` | DeepAgentsService.dll |
| `voice/delete_voice_clone` | agent_runtime_addon.node |
| `voice/release_voice_clone` | agent_runtime_addon.node |
| `voice/voice_clone_condition` | agent_runtime_addon.node |
| `watermark/get_watermark` | DeepAgentsService.dll |
| `zenith/submit_image_task` | DeepAgentsService.dll |

### 主机

```
github.com  x1
lv-api.ulikecam.com  x1
cacerts.digicert.com  x1
crl3.digicert.com  x1
www.digicert.com  x1
crl4.digicert.com  x1
sectigo.com  x1
crl.sectigo.com  x1
crt.sectigo.com  x1
crl.usertrust.com  x1
lv-pc-api.ulikecam.com  x1
crash.snssdk.com  x1
dig.bdurl.net  x1
tnc3-bjlgy.zijieapi.com  x1
tnc3-alisc1.zijieapi.com  x1
tnc3-aliec2.zijieapi.com  x1
lv.ulikecam.com  x1
lf9-cdn-tos.draftstatic.com  x1
sf1-cdn-tos.douyinstatic.com  x1
sf16-draftcdn-sg.ibytedtos.com  x1
```
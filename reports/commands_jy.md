# 剪映原生编辑命令表（从 app-server.mjs 抽取）

- 域：**18**
- 命令：**199**
- 模型可用安全子集：**26**

| 域 | 命令数 | 命令 |
| --- | ---: | --- |
| `video` | 56 | `add`<br>`setMaterial`<br>`setMask`<br>`clearMask`<br>`setOpacity`<br>`setBackgroundColor`<br>`setBackgroundBlur`<br>`setBackgroundImage`<br>`clearBackground`<br>`formatVideo`<br>`setTransition`<br>`updateTransition`<br>`clearTransition`<br>`setFade`<br>`denoiseOn`<br>`denoiseOff`<br>`addAnimation`<br>`updateAnimation`<br>`deleteAnimation`<br>`setSpeed`<br>`pitchOn`<br>`pitchOff`<br>`setCurveSpeed`<br>`seprateAudio`<br>`setMatting`<br>`clearMatting`<br>`reverse`<br>`crop`<br>`muteOn`<br>`muteOff`<br>`setBasicColor`<br>`resetBasicColor`<br>`setVolume`<br>`setFigure`<br>`setMakeupRoot`<br>`clearFigure`<br>`setFigureFaceId`<br>`setMix`<br>`setChromaColor`<br>`setChromaIntensity`<br>`setChromaShadow`<br>`setChromaEdgeSmooth`<br>`setChromaSpill`<br>`resetChroma`<br>`applyAllChroma`<br>`removeSmartCrop`<br>`addSmartCrop`<br>`setSmartColorAdjust`<br>`setStable`<br>`setVideoAlgorithm`<br>`addDigitalHuman`<br>`updateDigitalHuman`<br>`updateDigitalHumanRendered`<br>`addObjectLocked`<br>`updateObjectLocked`<br>`removeObjectLocked` |
| `audio` | 24 | `add`<br>`setVolume`<br>`setFade`<br>`denoiseOn`<br>`denoiseOff`<br>`pitchOn`<br>`pitchOff`<br>`setVoiceEffect`<br>`setVoiceEffectParams`<br>`clearVoiceEffect`<br>`setVoiceEffectToAll`<br>`setVocalSeparation`<br>`updateVocalSeparation`<br>`removeVocalSeparation`<br>`setVocalBeautify`<br>`updateVocalBeautify`<br>`resetVocalBeautify`<br>`removeVocalBeautify`<br>`setSpeed`<br>`modifiedToneOn`<br>`modifiedToneOff`<br>`setMaterial`<br>`addBeat`<br>`removeBeat` |
| `segment` | 19 | `move`<br>`scale`<br>`translate`<br>`rotate`<br>`updateLayout`<br>`split`<br>`insert`<br>`delete`<br>`mirror`<br>`setTimeRange`<br>`innerReplace`<br>`innerReplaceStack`<br>`paste`<br>`visible`<br>`mute`<br>`setName`<br>`duplicate`<br>`setDescription`<br>`multiSegmentsSetTimeRange` |
| `text` | 16 | `add`<br>`setMaterials`<br>`addSubtitles`<br>`setFixedSize`<br>`addAnimation`<br>`updateAnimation`<br>`deleteAnimation`<br>`addVideoTracker`<br>`updateVideoTracker`<br>`removeVideoTracker`<br>`deleteTextToAudioIds`<br>`updateSubtitleTemplate`<br>`resetSubtitleTemplate`<br>`updateEffect`<br>`setSubtitleKeywords`<br>`clearSubtitleKeywords` |
| `draft` | 14 | `setCanvasSize`<br>`setCanvasBackground`<br>`setCover`<br>`clearCover`<br>`setDraftName`<br>`setDraftId`<br>`setDraftUpdateTime`<br>`ensureDraftCanvasSize`<br>`updateDraftAIGCWatermark`<br>`clearDraft`<br>`setDraft`<br>`setAlignMode`<br>`setDraftKeywordsConfigs`<br>`setVideoGeneratorType` |
| `attachment` | 13 | `insertAsyncTasks`<br>`deleteAsyncTasks`<br>`updateAsyncTasksStatus`<br>`insertVideoAlgorithms`<br>`deleteVideoAlgorithms`<br>`updateVideoAlgorithm`<br>`insertAiWriterInfos`<br>`deleteAiWriterInfos`<br>`updateAiWriterInfo`<br>`setAiCreatorContent`<br>`updateAiCreation`<br>`updateAiReel`<br>`updateAiReelAgent` |
| `story` | 11 | `deleteAiStoryAlternative`<br>`addAiStoryAlternativeMaterials`<br>`cloneAiStoryAlternativeMaterials`<br>`deleteAiStoryAlternativeMaterials`<br>`updateAiStoryAlternativeMaterial`<br>`pinAiStoryAlternativeMaterial`<br>`updateMoveFeedsToAlternative`<br>`updateStoryId`<br>`innerReplace`<br>`innerReplaceStack`<br>`findInnerReplaceIds` |
| `textTemplate` | 8 | `add`<br>`setMaterial`<br>`addAnimation`<br>`updateAnimation`<br>`deleteAnimation`<br>`addVideoTracker`<br>`updateVideoTracker`<br>`removeVideoTracker` |
| `sticker` | 7 | `add`<br>`addAnimation`<br>`updateAnimation`<br>`deleteAnimation`<br>`addVideoTracker`<br>`updateVideoTracker`<br>`removeVideoTracker` |
| `undoRedo` | 6 | `undo`<br>`redo`<br>`canUndo`<br>`canRedo`<br>`getTopItemId`<br>`resetUndoRedo` |
| `track` | 4 | `add`<br>`delete`<br>`mute`<br>`updateTrackName` |
| `template` | 4 | `setMutableVideos`<br>`setMutableAudios`<br>`setMutableTexts`<br>`setTemplateMute` |
| `effect` | 3 | `add`<br>`updateAdjustParams`<br>`resetAdjustParams` |
| `adjustment` | 3 | `add`<br>`setBasicColor`<br>`resetBasicColor` |
| `keyframe` | 3 | `add`<br>`delete`<br>`update` |
| `templateCombination` | 3 | `templateCombinationAdd`<br>`replace`<br>`setSize` |
| `batch` | 3 | `batchStart`<br>`batchEnd`<br>`freezeVideo` |
| `filter` | 2 | `add`<br>`update` |

## 安全子集（模型只能调这些）

```
draft.setCanvasSize
draft.setDraftId
track.add
track.delete
track.mute
segment.move
segment.scale
segment.translate
segment.rotate
segment.updateLayout
segment.split
segment.delete
segment.setTimeRange
segment.innerReplace
segment.setDescription
video.add
video.muteOn
video.muteOff
video.setVolume
audio.add
audio.setVolume
text.add
undoRedo.undo
undoRedo.redo
undoRedo.canUndo
undoRedo.canRedo
```
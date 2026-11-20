# 达芬奇脚本 API 接口清单（解析自 DaVinciResolveScript.pyi）

- 类：**86**
- 方法：**530**

## 类一览

| 类 | 方法数 |
| --- | ---: |
| `TimelineItem` | 110 |
| `Timeline` | 70 |
| `Project` | 67 |
| `Resolve` | 50 |
| `MediaPoolItem` | 49 |
| `PhotoAlbumItem` | 48 |
| `MediaPool` | 32 |
| `ProjectManager` | 27 |
| `Graph` | 15 |
| `Folder` | 14 |
| `MediaStorage` | 11 |
| `PhotoAlbum` | 11 |
| `Gallery` | 8 |
| `ColorGroup` | 6 |
| `Effect` | 6 |
| `GalleryStillAlbum` | 6 |

## `ColorGroup`

| 方法 | 签名 | 返回 | 说明 |
| --- | --- | --- | --- |
| `GetName` | `self` | `str` | Returns the name of the ColorGroup |
| `SetName` | `self, groupName: str` | `bool` | Renames ColorGroup to groupName |
| `GetClipsInTimeline` | `self, timeline: Timeline | None = None` | `list[TimelineItem]` | Returns a list of TimelineItems in the ColorGroup for the given Timeline |
| `GetPhotosInPhotoAlbum` | `self, photoAlbum: PhotoAlbum | None = None` | `list[PhotoAlbumItem]` | Returns a list of PhotoAlbumItems in the ColorGroup for the given PhotoAlbum. Uses the current photo album if photoAlbum is omitted |
| `GetPreClipNodeGraph` | `self` | `Graph` | Returns the ColorGroup Pre-clip graph |
| `GetPostClipNodeGraph` | `self` | `Graph` | Returns the ColorGroup Post-clip graph |

## `Effect`

| 方法 | 签名 | 返回 | 说明 |
| --- | --- | --- | --- |
| `GetInfo` | `self` | `EffectInfo | None` | Returns information about the effect |
| `GetIsEnabled` | `self` | `bool` | Returns whether the effect is enabled |
| `SetIsEnabled` | `self, enabled: bool` | `bool` | Sets whether the effect is enabled |
| `GetFusionComp` | `self` | `FusionComp | None` | Returns the Fusion composition object for this effect, or None if it's not a Fusion effect |
| `GetIndex` | `self` | `int | None` | Returns the effect's 1-based index among its siblings' effects of the same category, or None if it's no longer applied |
| `SetIndex` | `self, index: int` | `bool` | Moves the effect to the given 1-based index among its sibling effects |

## `Folder`

| 方法 | 签名 | 返回 | 说明 |
| --- | --- | --- | --- |
| `GetName` | `self` | `str` | Returns the media folder name |
| `GetParentFolder` | `self` | `Folder` | Returns the Folder object containing this folder, or None for the root folder. |
| `GetSubFolderList` | `self` | `list[Folder]` | Returns a list of subfolders in the folder |
| `GetClipList` | `self` | `list[MediaPoolItem]` | Returns a list of clips (items) within the folder |
| `GetIsFolderStale` | `self` | `bool` | Returns true if folder is stale in collaboration mode |
| `GetUniqueId` | `self` | `str` | Returns a unique ID for the media pool folder |
| `Export` | `self, filePath: str` | `bool` | Exports the folder as a DRB file to filePath |
| `TranscribeAudio` | `self, useSpeakerDetection: bool | None = None, transcribeAsNestedClip = False` | `bool` | Transcribes audio of the MediaPoolItems within the folder and nested folders. |
| `ClearTranscription` | `self` | `bool` | Clears audio transcription of the MediaPoolItems within the folder and nested folders. |
| `PerformAudioClassification` | `self` | `bool` | Analyzes and classifies the audio of the MediaPoolItems within the folder and nested folders into categories and subcategories |
| `ClearAudioClassification` | `self` | `bool` | Clears audio classification of the MediaPoolItems within the folder and nested folders |
| `RemoveMotionBlur` | `self, deblurOption: DeblurOptions | None = None` | `list[list[MediaPoolItem]]` | Apply Motion Deblur on MediaPoolItems in Folder, Returns a list of original to newly created MediaPoolItems |
| `AnalyzeForIntellisearch` | `self, identifyFaces: bool, isBetterMode: bool` | `bool` | Perform Intellisearch analysis to all the MediaPoolItems in the folder. |
| `AnalyzeForSlate` | `self, markerColor: SlateMarkerColor` | `bool` | Perform Slate analysis with current settings and use the stated markerColor to all the MediaPoolItems in the folder. Adds a 'Detected Slate' duration marker ove |

## `Gallery`

| 方法 | 签名 | 返回 | 说明 |
| --- | --- | --- | --- |
| `GetAlbumName` | `self, galleryStillAlbum: GalleryStillAlbum` | `str` | Returns the name of a GalleryStillAlbum object |
| `SetAlbumName` | `self, galleryStillAlbum: GalleryStillAlbum, albumName: str` | `bool` | Sets the name of a GalleryStillAlbum object |
| `GetCurrentStillAlbum` | `self` | `GalleryStillAlbum` | Returns current album as a GalleryStillAlbum object |
| `SetCurrentStillAlbum` | `self, galleryStillAlbum: GalleryStillAlbum` | `bool` | Sets current album to the given GalleryStillAlbum object |
| `CreateGalleryStillAlbum` | `self` | `GalleryStillAlbum` | Creates a new gallery still album |
| `CreateGalleryPowerGradeAlbum` | `self` | `GalleryStillAlbum` | Creates a new gallery power grade album |
| `GetGalleryStillAlbums` | `self` | `list[GalleryStillAlbum]` | Returns the gallery still albums as a list of GalleryStillAlbum objects |
| `GetGalleryPowerGradeAlbums` | `self` | `list[GalleryStillAlbum]` | Returns the gallery PowerGrade albums as a list of GalleryStillAlbum objects |

## `GalleryStillAlbum`

| 方法 | 签名 | 返回 | 说明 |
| --- | --- | --- | --- |
| `GetStills` | `self` | `list[GalleryStill]` | Returns the list of GalleryStill objects in the album |
| `GetLabel` | `self, galleryStill: GalleryStill` | `str` | Returns the label of the galleryStill |
| `SetLabel` | `self, galleryStill: GalleryStill, label: str` | `bool` | Sets the new label to a GalleryStill object |
| `ImportStills` | `self, filePaths: list[str]` | `bool` | Imports GalleryStill from each filePath in the list |
| `ExportStills` | `self, galleryStill: list[GalleryStill], folderPath: str, filePrefix: str, format: str` | `bool` | Exports list of GalleryStill objects to a directory |
| `DeleteStills` | `self, galleryStill: list[GalleryStill]` | `bool` | Deletes specified list of GalleryStill objects |

## `Graph`

| 方法 | 签名 | 返回 | 说明 |
| --- | --- | --- | --- |
| `GetNumNodes` | `self` | `int` | Returns the number of nodes in the graph |
| `SetLUT` | `self, nodeIndex: int, lutPath: str` | `bool` | Sets LUT on the node mapping the node index provided, 1 <= nodeIndex <= GetNumNodes() |
| `GetLUT` | `self, nodeIndex: int` | `str` | Gets relative LUT path based on the node index provided, 1 <= nodeIndex <= GetNumNodes() |
| `SetNodeCacheMode` | `self, nodeIndex: int, cacheValue: CacheMode` | `bool` | Sets the cache mode type on the node mapping the node index provided |
| `GetNodeCacheMode` | `self, nodeIndex: int` | `int` | Returns the cache mode type on the node mapping the node index provided |
| `GetNodeLabel` | `self, nodeIndex: int` | `str` | Returns the label of the node at nodeIndex |
| `SetNodeLabel` | `self, nodeIndex: int, label: str` | `bool` | Sets the label of the node at nodeIndex, 1 <= nodeIndex <= GetNumNodes() |
| `GetNodeColor` | `self, nodeIndex: int` | `NodeColor | Literal['']` | Returns the color of the node at nodeIndex as a string, or an empty string if no color is set |
| `SetNodeColor` | `self, nodeIndex: int, colorName: NodeColor | Literal['']` | `bool` | Sets the color of the node at nodeIndex based on the colorName (string). An empty string clears the color. 1 <= nodeIndex <= GetNumNodes() |
| `GetToolsInNode` | `self, nodeIndex: int` | `list[str]` | Returns the list of tools the node at nodeIndex uses, as the node tooltip shows them: the applied LUT ('LUT: name'), the OFX plugin ('OFX: name') and every grou |
| `SetNodeEnabled` | `self, nodeIndex: int, isEnabled: bool` | `bool` | Sets the node at the given nodeIndex to isEnabled, 1 <= nodeIndex <= GetNumNodes() |
| `GetNodeEnabled` | `self, nodeIndex: int` | `bool` | Returns whether the node at the given nodeIndex is enabled, 1 <= nodeIndex <= GetNumNodes() |
| `ApplyArriCdlLut` | `self` | `bool` | Applies ARRI CDL and LUT. |
| `ApplyGradeFromDRX` | `self, path: str, gradeMode: int, applyToAllLayers = False, keyframeMode = Resolve.KEYFRAME_MODE_ALL` | `bool` | Loads a still from given file path and applies grade to graph with gradeMode (0=No keyframes, 1=Source Timecode aligned, 2=Start Frames aligned). If applyToAllL |
| `ResetAllGrades` | `self` | `bool` | Resets all grades in the graph. Node labels are cleared too |

## `MediaPool`

| 方法 | 签名 | 返回 | 说明 |
| --- | --- | --- | --- |
| `AddSubFolder` | `self, folder: Folder, name: str` | `Folder | None` | Adds new subfolder under specified Folder object with the given name. A name already used by another subfolder is accepted and adds a second subfolder with that |
| `GetCurrentFolder` | `self` | `Folder` | Returns currently selected Folder |
| `RefreshFolders` | `self` | `bool` | Updates the folders in collaboration mode |
| `SetCurrentFolder` | `self, folder: Folder` | `bool` | Sets current folder by given Folder |
| `GetRootFolder` | `self` | `Folder` | Returns root Folder of Media Pool |
| `CreateTimelineFromClips` | `self, name: str, clipInfos: list[CreateTimelineClipInfo]` | `Timeline` | Creates new timeline with specified name, and appends the specified MediaPoolItem objects |
| `AppendToTimeline` | `self, clipInfos: list[AppendClipInfo]` | `list[TimelineItem]` | Appends specified MediaPoolItem objects in the current timeline. Returns the list of appended timelineItems |
| `CreateEmptyTimeline` | `self, name: str, timecode: str | None = None` | `Timeline | None` | Adds new timeline with given name. Returns None if the timeline could not be created, which includes the name being empty, already used by another timeline, or  |
| `ImportTimelineFromFile` | `self, filePath: str, importOptions: ImportOptions | None = None` | `Timeline` | Creates timeline based on parameters within given file (AAF/EDL/XML/FCPXML/DRT/ADL/OTIO) and optional importOptions dict |
| `DeleteTimelines` | `self, timelines: list[Timeline]` | `bool` | Deletes specified timelines in the media pool |
| `CreateEmptyPhotoAlbum` | `self, name: str` | `PhotoAlbum` | Adds new photo album with given name |
| `CreatePhotoAlbumFromPhotos` | `self, name: str, photos: list[MediaPoolItem]` | `PhotoAlbum` | Creates new photo album with specified name, and adds the specified still image MediaPoolItem objects |
| `DeletePhotoAlbums` | `self, photoAlbums: list[PhotoAlbum]` | `bool` | Deletes specified photo albums in the media pool |
| `AddToPhotoAlbum` | `self, photos: list[MediaPoolItem]` | `list[PhotoAlbumItem]` | Adds specified still image MediaPoolItem objects to the current photo album. Returns the list of added photoAlbumItems |
| `ExportMetadata` | `self, fileName: str, clips: list[MediaPoolItem] | None = None` | `bool` | Exports metadata of specified clips to 'fileName' in CSV format. If no clips are specified, all clips from media pool will be used |
| `DeleteClips` | `self, clips: list[MediaPoolItem]` | `bool` | Deletes specified clips or timeline mattes in the media pool |
| `ImportFolderFromFile` | `self, filePath: str, sourceClipsPath: str | None = None` | `bool` | Imports a DRB folder from the given file path |
| `DeleteFolders` | `self, subfolders: list[Folder]` | `bool` | Deletes specified subfolders in the media pool |
| `MoveClips` | `self, clips: list[MediaPoolItem], targetFolder: Folder` | `bool` | Moves specified clips to target folder |
| `MoveFolders` | `self, folders: list[Folder], targetFolder: Folder` | `bool` | Moves specified folders to target folder |
| `GetClipMatteList` | `self, mediaPoolItem: MediaPoolItem` | `list[str]` | Get mattes for specified MediaPoolItem, as a list of paths to the matte files |
| `GetTimelineMatteList` | `self, folder: Folder` | `list[MediaPoolItem]` | Get mattes in specified Folder, as list of MediaPoolItems |
| `DeleteClipMattes` | `self, mediaPoolItem: MediaPoolItem, paths: list[str]` | `bool` | Delete mattes based on their file paths, for specified MediaPoolItem |
| `RelinkClips` | `self, clips: list[MediaPoolItem], folderPath: str` | `bool` | Update the folder location of specified media pool clips with the specified folder path |
| `UnlinkClips` | `self, clips: list[MediaPoolItem]` | `bool` | Unlink specified media pool clips |
| `ImportMedia` | `self, clipInfos: list[ImportClipInfo]` | `list[MediaPoolItem]` | Imports specified file/folder paths into current Media Pool folder. Returns a list of the MediaPoolItems created |
| `GetUniqueId` | `self` | `str` | Returns a unique ID for the media pool |
| `CreateStereoClip` | `self, leftMediaPoolItem: MediaPoolItem, rightMediaPoolItem: MediaPoolItem` | `MediaPoolItem` | Takes in two existing media pool items and creates a new 3D stereoscopic media pool entry replacing the input media |
| `CreateMulticamClip` | `self, clips: list[MediaPoolItem], multicamOptions: MulticamOptions` | `list[MediaPoolItem]` | Creates Multicam clips from the specified MediaPoolItems and options |
| `AutoSyncAudio` | `self, mediaPoolItems: list[MediaPoolItem], audioSyncSettings: AudioSyncSettings` | `bool` | Syncs audio for specified MediaPoolItems. The list must contain at least one video and one audio clip. |
| `GetSelectedClips` | `self` | `list[MediaPoolItem]` | Returns the current selected MediaPoolItems |
| `SetSelectedClip` | `self, mediaPoolItem: MediaPoolItem` | `bool` | Sets the selected MediaPoolItem to the given MediaPoolItem |

## `MediaPoolItem`

| 方法 | 签名 | 返回 | 说明 |
| --- | --- | --- | --- |
| `GetName` | `self` | `str` | Returns the clip name. |
| `SetName` | `self, name: str` | `bool` | Sets the clip's name to name(string). |
| `GetTimeline` | `self` | `Timeline` | Returns the timeline object if the mpItem is a timeline clip |
| `GetPhotoAlbum` | `self` | `PhotoAlbum | None` | Returns the photo album object if the mpItem is a photo album clip |
| `GetParentFolder` | `self` | `Folder` | Returns the Folder object containing this media pool item. |
| `GetMetadata` | `self, metadataType: str | None = None` | `str | dict` | Returns the metadata value for the key 'metadataType'. If no argument is specified, a dict of all set metadata properties is returned. |
| `SetMetadata` | `self, metadata: dict` | `bool` | Sets the item metadata with specified dict of key-value pairs |
| `GetThirdPartyMetadata` | `self, metadataType: str | None = None` | `str | dict` | Returns the third party metadata value for the key 'metadataType'. If no argument, a dict of all set third party metadata properties is returned. |
| `SetThirdPartyMetadata` | `self, metadata: dict` | `bool` | Sets/Add the item third party metadata with specified dict of key-value pairs |
| `GetMediaId` | `self` | `str` | Returns the unique ID for the MediaPoolItem. |
| `AddMarker` | `self, frameId: int, color: MarkerColor, name: str, note: str, duration: int, customData: str | None = None` | `bool` | Creates a new marker at given frameId position. 'customData' is optional. |
| `DeleteMarkersByColor` | `self, color: MarkerColor | Literal['All']` | `bool` | Delete all markers of the specified color. 'All' as argument deletes all color markers. |
| `ExportFrame` | `self, frameOffset: int, exportFrameOptions: ExportFrameOptions | None = None` | `ExportFrameResult` | Exports the frame at frameOffset (0-based offset from the item start) as a still image per exportFrameOptions. |
| `ExportThumbnails` | `self, frames: list[int | ThumbnailFrame], exportThumbnailsOptions: ExportThumbnailsOptions | None = None` | `ExportThumbnailsResult` | Renders the given frames (0-based offsets from the item start) into a single grid image, filled in the order given |
| `DeleteMarkerAtFrame` | `self, frameNum: int` | `bool` | Delete marker at frame number from the media pool item. |
| `DeleteMarkerByCustomData` | `self, customData: str` | `bool` | Delete first matching marker with specified customData. |
| `GetMarkers` | `self` | `dict[int, MarkerInfo]` | Returns a dict (frameId -> {information}) of all markers. |
| `GetMarkerByCustomData` | `self, customData: str` | `MarkerInfo` | Returns marker {information} for the first matching marker with specified customData. |
| `UpdateMarkerCustomData` | `self, frameId: int, customData: str` | `bool` | Updates customData for the marker at given frameId position. |
| `GetMarkerCustomData` | `self, frameId: int` | `str` | Returns customData string for the marker at given frameId position. |
| `AddFlag` | `self, color: FlagColor` | `bool` | Adds a flag with given color (string). |
| `GetFlagList` | `self` | `list[str]` | Returns a list of flag colors assigned to the item. |
| `ClearFlags` | `self, color: FlagColor | Literal['All']` | `bool` | Clears the flag of the given color if one exists. An 'All' argument is supported and clears all flags. |
| `GetClipColor` | `self` | `ClipColor | Literal['']` | Returns the item color as a string. |
| `SetClipColor` | `self, colorName: ClipColor` | `bool` | Sets the item color based on the colorName (string). |
| `ClearClipColor` | `self` | `bool` | Clears the item color. |
| `LinkFullResolutionMedia` | `self, fullResMediaPath: str` | `bool` | Links proxy media to full resolution media files specified via its path. |
| `LinkProxyMedia` | `self, proxyMediaFilePath: str` | `bool` | Links proxy media located at path specified by arg 'proxyMediaFilePath' with the current clip. |
| `UnlinkProxyMedia` | `self` | `bool` | Unlinks any proxy media associated with clip. |
| `ReplaceClip` | `self, filePath: str` | `bool` | Replaces the underlying asset and metadata of MediaPoolItem with the specified absolute clip path. |
| `ReplaceClipPreserveSubClip` | `self, filePath: str` | `bool` | Replaces the underlying asset and metadata preserving original sub clip extents. |
| `GetClipProperty` | `self, propertyName: str | None = None` | `str | ClipProperties` | Returns the property value for the key 'propertyName'. If no argument, a dict of all clip properties is returned. |
| `SetClipProperty` | `self, propertyName: str, propertyValue: str` | `bool` | Sets the given property to propertyValue (string). |
| `GetUniqueId` | `self` | `str` | Returns a unique ID for the media pool item |
| `TranscribeAudio` | `self, useSpeakerDetection: bool | None = None, transcribeAsNestedClip = False` | `bool` | Transcribes audio of the MediaPoolItem |
| `ClearTranscription` | `self, clearNestedClipTranscription = False` | `bool` | Clears audio transcription of the MediaPoolItem. |
| `PerformAudioClassification` | `self` | `bool` | Analyzes and classifies the audio of a MediaPoolItem. |
| `ClearAudioClassification` | `self` | `bool` | Clears audio classification of the MediaPoolItem. |
| `GetAudioMapping` | `self` | `str` | Returns a string with MediaPoolItem's audio mapping information (JSON format). |
| `SetAudioMapping` | `self, audioMapping: str` | `bool` | Sets audio mapping from a JSON string. |
| `GetMarkInOut` | `self` | `MarkInOut` | Returns dict of in/out marks set. |
| `SetMarkInOut` | `self, markIn: int, markOut: int, markType: MarkType | None = None` | `bool` | Sets mark in/out of type MarkType (default: 'all'). |
| `ClearMarkInOut` | `self, markType: MarkType | None = None` | `bool` | Clears mark in/out of type MarkType (default: 'all'). |
| `MonitorGrowingFile` | `self` | `bool` | Monitor a file as long as it keeps growing. |
| `RemoveMotionBlur` | `self, deblurOption: DeblurOptions` | `MediaPoolItem` | Apply Motion Deblur on MediaPoolItem, Returns newly created MediaPoolItem. |
| `AnalyzeForIntellisearch` | `self, identifyFaces: bool, isBetterMode: bool` | `bool` | Perform Intellisearch analysis on the MediaPoolItem. |
| `AnalyzeForSlate` | `self, markerColor: SlateMarkerColor` | `bool` | Perform Slate analysis on the MediaPoolItem, adding a 'Detected Slate' duration marker in markerColor over the frames of each slate found. The text written on t |
| `GetTranscription` | `self, useNestedClipTranscription = False` | `Transcription` | Returns transcription data for the media pool item if available. |
| `SetTranscription` | `self, transcription: Transcription` | `bool` | Replaces the transcription of the MediaPoolItem. Timelines are transcribed as a nested clip. See README.md section 'Setting a Transcription'. |

## `MediaStorage`

| 方法 | 签名 | 返回 | 说明 |
| --- | --- | --- | --- |
| `GetMountedVolumeList` | `self` | `list[str]` | Returns list of folder paths corresponding to mounted volumes displayed in Resolve's Media Storage |
| `GetSubFolderList` | `self, folderPath: str` | `list[str]` | Returns list of folder paths in the given absolute folder path |
| `GetFileList` | `self, folderPath: str` | `list[str]` | Returns list of media and file listings in the given absolute folder path |
| `RevealInStorage` | `self, path: str` | `bool` | Expands and displays given file/folder path in Resolve's Media Storage |
| `AddItemListToMediaPool` | `self, itemInfos: list[MediaStorageItemInfo]` | `list[MediaPoolItem]` | Adds specified file/folder paths from Media Storage into current Media Pool folder. Returns a list of the MediaPoolItems created |
| `AddClipMattesToMediaPool` | `self, mediaPoolItem: MediaPoolItem, paths: list[str], stereoEye: str | None = None` | `bool` | Adds specified media files as mattes for the specified MediaPoolItem. stereoEye is 'left' or 'right' for stereo clips |
| `AddTimelineMattesToMediaPool` | `self, paths: list[str]` | `list[MediaPoolItem]` | Adds specified media files as timeline mattes in current media pool folder. Returns a list of created MediaPoolItems |
| `StartCloneMedia` | `self, sourceDir: str, targetDirs: str | list[str]` | `bool` | Starts cloning media from sourceDir to targetDirs. Use SetCloneToolSettings to configure PreserveFolderName/ChecksumType beforehand. |
| `SetCloneToolSettings` | `self, cloneToolSettings: CloneToolSettings | None = None` | `bool` | Sets the PreserveFolderName/ChecksumType options used by subsequent StartCloneMedia calls (and by the Clone Tool UI). |
| `StopCloneMedia` | `self` | `bool` | Stops the currently in-progress clone job started via StartCloneMedia. Returns False if no clone job is in progress. |
| `GetCloneStatus` | `self` | `CloneStatus` | Returns a dict with the status of the current (or most recently started) clone job |

## `PhotoAlbum`

| 方法 | 签名 | 返回 | 说明 |
| --- | --- | --- | --- |
| `GetName` | `self` | `str` | Returns the photo album name. |
| `SetName` | `self, photoAlbumName: str` | `bool` | Sets the photo album name if photoAlbumName (string) is unique. |
| `GetUniqueId` | `self` | `str` | Returns a unique ID for the photo album |
| `GetPhotoList` | `self` | `list[PhotoAlbumItem]` | Returns a list of photo album items in the photo album. |
| `ExportThumbnails` | `self, photoIndices: list[int], exportThumbnailsOptions: ExportThumbnailsOptions | None = None` | `ExportThumbnailsResult` | Renders the photos at the given 1-based album positions into a single grid image, one cell per photo labelled with its position, 1 <= photoIndex <= GetPhotoList |
| `GetCurrentItem` | `self` | `PhotoAlbumItem | None` | Returns the current photo album item. |
| `DeletePhotos` | `self, photoAlbumItems: list[PhotoAlbumItem]` | `bool` | Deletes specified PhotoAlbumItems from the photo album. |
| `GetNodeGraph` | `self` | `Graph` | Returns the photo album's node graph object. |
| `GetMediaPoolItem` | `self` | `MediaPoolItem | None` | Returns the media pool item corresponding to the photo album |
| `GrabStill` | `self` | `GalleryStill` | Grabs still from the current photo. Returns a GalleryStill object. |
| `GrabAllStills` | `self` | `list[GalleryStill]` | Grabs stills from all photos in the photo album. |

## `PhotoAlbumItem`

| 方法 | 签名 | 返回 | 说明 |
| --- | --- | --- | --- |
| `GetName` | `self` | `str` | Returns the item name |
| `SetName` | `self, name: str` | `bool` | Sets the photo's name to name. |
| `GetUniqueId` | `self` | `str` | Returns a unique ID for the photo album item |
| `GetFusionCompCount` | `self` | `int` | Returns number of Fusion compositions associated with the photo album item |
| `GetFusionCompNameList` | `self` | `list[str]` | Returns a list of Fusion composition names associated with the photo album item |
| `GetFusionCompByIndex` | `self, compIndex: int` | `FusionComp | None` | Returns the Fusion composition object based on given index. 1 <= compIndex <= photoAlbumItem.GetFusionCompCount() |
| `GetFusionCompByName` | `self, compName: str` | `FusionComp | None` | Returns the Fusion composition object based on given name |
| `AddFusionComp` | `self` | `FusionComp` | Adds a new Fusion composition associated with the photo album item |
| `DeleteFusionCompByName` | `self, compName: str` | `bool` | Deletes the named Fusion composition |
| `LoadFusionCompByName` | `self, compName: str` | `FusionComp` | Loads the named Fusion composition as the active composition |
| `RenameFusionCompByName` | `self, oldName: str, newName: str` | `bool` | Renames the Fusion composition identified by oldName |
| `ImportFusionComp` | `self, path: str` | `FusionComp` | Imports a Fusion composition from given file path by creating and adding a new composition for the item |
| `ExportFusionComp` | `self, path: str, compIndex: int` | `bool` | Exports the Fusion composition based on given index to the path provided |
| `GetMediaPoolItem` | `self` | `MediaPoolItem | None` | Returns the media pool item corresponding to the photo album item if one exists |
| `AddFlag` | `self, color: FlagColor` | `bool` | Adds a flag with given color (string) |
| `GetFlagList` | `self` | `list[str]` | Returns a list of flag colors assigned to the item |
| `ClearFlags` | `self, color: FlagColor | Literal['All']` | `bool` | Clears flags of the specified color. An 'All' argument is supported to clear all flags |
| `GetClipColor` | `self` | `ClipColor | Literal['']` | Returns the item color as a string |
| `SetClipColor` | `self, colorName: ClipColor` | `bool` | Sets the item color based on the colorName (string) |
| `ClearClipColor` | `self` | `bool` | Clears the item color |
| `CopyGrades` | `self, tgtPhotoAlbumItems: list[PhotoAlbumItem]` | `bool` | Copies the current node stack layer grade to the same layer for each item in tgtPhotoAlbumItems. |
| `ApplyAutoColor` | `self` | `bool` | Analyses the photo and applies the automatic balance and grade. Replaces the grade of a previous call and clears the legacy auto color values. |
| `SetAutoColorEnabled` | `self, enabled: bool` | `bool` | Enables or disables the grade a previous ApplyAutoColor() applied |
| `GetAutoColorEnabled` | `self` | `bool | None` | Returns whether auto color is applied and enabled, none if it has no auto color |
| `ClearAutoColor` | `self` | `bool` | Discards auto-color grades |
| `GetCurrentVersion` | `self` | `VersionInfo` | Returns the current version of the photo. The returned value will have the keys versionName and versionType (always 1 - remote, as photo albums only support rem |
| `RenameVersionByName` | `self, oldName: str, newName: str` | `bool` | Renames the color version identified by oldName. Photo albums only support remote versions |
| `DeleteVersionByName` | `self, versionName: str` | `bool` | Deletes a color version by name. Photo albums only support remote versions |
| `LoadVersionByName` | `self, versionName: str` | `bool` | Loads a named color version as the active version. Photo albums only support remote versions |
| `AddVersion` | `self, versionName: str` | `bool` | Adds a new color version for a photo. Photo albums only support remote versions |
| `GetVersionNameList` | `self` | `list[str]` | Returns a list of all color versions. Photo albums only support remote versions |
| `SetCDL` | `self, CDL: CDL` | `bool` | Sets CDL values on the node. Keys of map are: 'NodeIndex', 'Slope', 'Offset', 'Power', 'Saturation' |
| `GetCDL` | `self, nodeIndex: int` | `CDL` | Returns the ASC CDL equivalent of the primaries of the node at nodeIndex, as the dict |
| `GetNodeGraph` | `self, layerIdx: int | None = None` | `Graph` | Returns the photo's node graph object at layerIdx (int, optional). Returns the first layer if layerIdx is skipped. 1 <= layerIdx <= project.GetSetting('nodeStac |
| `ResetAllNodeColors` | `self` | `bool` | Resets node color for all nodes in the active version of the photo. |
| `ExportLUT` | `self, exportType: ExportLutType, path: str` | `bool` | Exports a LUT of the size given by 'exportType', saving it in the provided 'path' |
| `GetColorGroup` | `self` | `ColorGroup | None` | Returns the photo's color group if one exists |
| `AssignToColorGroup` | `self, colorGroup: ColorGroup` | `bool` | Assigns the photo to the given ColorGroup. ColorGroup must be an existing group in the current project |
| `RemoveFromColorGroup` | `self` | `bool` | Removes the photo from its ColorGroup |
| `LoadBurnInPreset` | `self, presetName: str` | `bool` | Loads user defined data burn in preset for photo when supplied presetName (string). |
| `GetRatings` | `self` | `int` | Returns the photo rating in stars (0-5) |
| `SetRatings` | `self, stars: int` | `bool` | Sets the photo rating to stars (int, 0-5) |
| `AddEffect` | `self, category: str, id: str` | `Effect | None` | Applies the effect with the provided category and id (see Resolve.GetEffectsList) to this photo album item |
| `GetEffects` | `self, category: str` | `list[Effect]` | Returns the effects of the given category ('fusion' or 'ofx') applied to this photo album item |
| `DeleteEffects` | `self, effects: list[Effect]` | `bool` | Removes the given effects from this photo album item |
| `ExportFrame` | `self, exportFrameOptions: ExportFrameOptions | None = None` | `ExportFrameResult` | Exports the photo as a still image per exportFrameOptions. |
| `GetProperties` | `self` | `PhotoAlbumItemProperties` | Returns a dict with all supported photo properties (source transform, cropping and looks). See README.md section 'Looking up Photo Album Item properties'. |
| `SetProperties` | `self, properties: PhotoAlbumItemProperties` | `bool` | Sets the photo properties (source transform, cropping and looks) with the specified dict of property keys and values. See README.md section 'Looking up Photo Al |

## `Project`

| 方法 | 签名 | 返回 | 说明 |
| --- | --- | --- | --- |
| `GetMediaPool` | `self` | `MediaPool` | Returns the MediaPool object |
| `GetCurrentTimeline` | `self` | `Timeline` | Returns the currently loaded timeline |
| `SetCurrentTimeline` | `self, timeline: Timeline` | `bool` | Sets given timeline as current timeline for the project |
| `GetTimelineCount` | `self` | `int` | Returns the number of timelines in the project |
| `GetTimelineByIndex` | `self, idx: int` | `Timeline | None` | Returns timeline at the given index, 1 <= idx <= project.GetTimelineCount() |
| `GetPhotoAlbumCount` | `self` | `int` | Returns the number of photo albums in the project |
| `GetPhotoAlbumByIndex` | `self, idx: int` | `PhotoAlbum | None` | Returns photo album at the given index, 1 <= idx <= project.GetPhotoAlbumCount() |
| `GetCurrentPhotoAlbum` | `self` | `PhotoAlbum | None` | Returns the currently loaded photo album |
| `SetCurrentPhotoAlbum` | `self, photoAlbum: PhotoAlbum` | `bool` | Sets given photo album as current photo album for the project |
| `GetGallery` | `self` | `Gallery` | Returns the Gallery object |
| `GetName` | `self` | `str` | Returns project name |
| `SetName` | `self, projectName: str` | `bool` | Sets project name if given projectName is unique |
| `GetProjectSettingsPresetList` | `self` | `list[ProjectSettingsPresetInfo]` | Returns a list of project settings presets and their information |
| `SetProjectSettingsPreset` | `self, presetName: str` | `bool` | Sets project settings preset by given name into project |
| `DeleteProjectSettingsPreset` | `self, presetName: str` | `bool` | Deletes the project settings preset with the given name |
| `SaveCurrentProjectSettingsAsNewPreset` | `self, presetName: str` | `bool` | Saves the current project settings as a new preset with the given name |
| `UpdateProjectSettingsPreset` | `self, presetName: str` | `bool` | Updates the given project settings preset with current settings |
| `ExportProjectSettingsPreset` | `self, presetName: str, exportPath: str` | `bool` | Exports the given project settings preset to the specified file path |
| `ImportProjectSettingsPreset` | `self, presetFilePath: str, presetName: str | None = None` | `bool` | Imports a project settings preset from file. Uses file base name as preset name if not specified. |
| `GetRenderJobList` | `self` | `list[RenderJobInfo]` | Returns a list of render jobs and their information |
| `GetRenderPresetList` | `self` | `list[str]` | Returns a list of render preset names |
| `LoadRenderPreset` | `self, presetName: str` | `bool` | Loads a render preset by name |
| `SaveAsNewRenderPreset` | `self, presetName: str` | `bool` | Saves current render settings as a new preset with the given name |
| `DeleteRenderPreset` | `self, presetName: str` | `bool` | Deletes given render preset |
| `UpdateRenderPreset` | `self, presetName: str` | `bool` | Updates given render preset with current render settings |
| `SetQuickExportEnabledForRenderPreset` | `self, presetName: str, isEnabled: bool` | `bool` | Enables or disables quick export for the named render preset |
| `StartRendering` | `self, jobIds: list[str], isInteractiveMode = False` | `bool` | Starts rendering jobs indicated by the input job ids |
| `StopRendering` | `self` | `` | Stops any current render processes |
| `IsRenderingInProgress` | `self` | `bool` | Returns True if a rendering is in progress |
| `AddRenderJob` | `self` | `str` | Adds a render job based on current render settings to the render queue |
| `DeleteRenderJob` | `self, jobId: str` | `bool` | Deletes render job for input job id |
| `DeleteAllRenderJobs` | `self` | `bool` | Deletes all render jobs in the queue |
| `SetRenderSettings` | `self, settings: RenderSettings` | `bool` | Sets given settings for rendering |
| `GetRenderResolutions` | `self, format: str | None = None, codec: str | None = None` | `list[ResolutionInfo]` | Returns list of resolutions applicable for the given render format and codec |
| `GetSettings` | `self` | `ProjectSettings` | Returns a dict with all project settings. See README.md section 'Looking up Project and Clip properties'. |
| `SetSettings` | `self, settings: ProjectSettings` | `bool` | Sets the project settings with specified dict of setting names and values. See README.md section 'Looking up Project and Clip properties'. |
| `GetRenderJobStatus` | `self, jobId: str` | `RenderJobStatus` | Returns a dict with job status and completion percentage |
| `GetQuickExportRenderPresets` | `self` | `list[str]` | Returns a list of quick export render presets |
| `RenderWithQuickExport` | `self, quickExportPresetName: str, presetInfo: QuickExportRenderSettings` | `QuickExportRenderStatus` | Renders current timeline with quick export preset |
| `GetRenderWithQuickExportStatus` | `self` | `QuickExportRenderStatus` | Returns progress information for active RenderWithQuickExport operation |
| `GetPhotoQuickExportRenderPresets` | `self` | `list[str]` | Returns a list of quick export render presets for photo albums |
| `SetPhotoRenderSettings` | `self, settings: PhotoRenderSettings` | `bool` | Sets given settings for rendering the current photo album, settings not given keep their current value |
| `RenderPhotosWithQuickExport` | `self, quickExportPresetName: str, presetInfo: PhotoQuickExportRenderSettings` | `QuickExportRenderStatus` | Renders current photo album with quick export preset |
| `GetRenderFormats` | `self` | `dict` | Returns a dict (format -> file extension) of available render formats |
| `GetAudioRenderFormats` | `self` | `dict` | Returns a dict (format -> file extension) of available audio render formats |
| `GetRenderCodecs` | `self, renderFormatFileExtension: str` | `dict` | Returns a dict (codec description -> codec name) of available codecs |
| `GetAudioRenderCodecs` | `self, audioRenderFormatFileExtension: str` | `dict` | Returns a dict (codec description -> codec name) of available audio codecs for the given format |
| `GetCurrentRenderFormatAndCodec` | `self` | `dict[str, str]` | Returns a dict with currently selected format and render codec |
| `SetCurrentRenderFormatAndCodec` | `self, format: str, codec: str` | `bool` | Sets given render format and render codec as options for rendering |
| `GetCurrentRenderMode` | `self` | `int` | Returns the render mode: 0 - Individual clips, 1 - Single clip |
| `SetCurrentRenderMode` | `self, renderMode: int` | `bool` | Sets the render mode: 0 for Individual clips, 1 for Single clip |
| `RefreshLUTList` | `self` | `bool` | Refreshes LUT List |
| `GetUniqueId` | `self` | `str` | Returns a unique ID for the project item |
| `InsertAudioToCurrentTrackAtPlayhead` | `self, mediaPath: str, startOffsetInSamples: int, durationInSamples: int` | `bool` | Inserts the media with startOffset and duration in samples to the current track at the playhead |
| `LoadBurnInPreset` | `self, presetName: str` | `bool` | Loads user defined data burn in preset |
| `ExportCurrentFrameAsStill` | `self, filePath: str` | `bool` | Exports current frame as still to supplied filePath |
| `GetColorGroupsList` | `self` | `list[ColorGroup]` | Returns a list of all group objects in the timeline |
| `AddColorGroup` | `self, groupName: str` | `ColorGroup` | Creates a new ColorGroup with unique groupName |
| `DeleteColorGroup` | `self, colorGroup: ColorGroup` | `bool` | Deletes the given ColorGroup and sets clips to ungrouped |
| `ApplyFairlightPresetToCurrentTimeline` | `self, presetName: str` | `bool` | Applies Fairlight preset to current timeline |
| `ResetIntellisearchAnalysis` | `self` | `bool` | Resets intellisearch analysis for the project |
| `GenerateSpeech` | `self, speechSettings: SpeechSettings, timecode: str | None = None` | `MediaPoolItem | None` | Generates speech for given speechSettings dict. Requires the 'AI Speech Generator' Extra to be installed; without it the call fails instead of returning a Media |
| `GetTranscribeAudioStatus` | `self` | `TranscribeAudioStatus` | Returns a dict with job status and completion percentage of the active TranscribeAudio operation |
| `GetAnalyzeForSlateStatus` | `self` | `SlateAnalysisStatus` | Returns a dict with job status and completion percentage of the active AnalyzeForSlate operation |
| `GetSmartReframeStatus` | `self` | `SmartReframeStatus` | Returns a dict with job status and completion percentage of the active SmartReframe operation |
| `GetDetectSceneCutsStatus` | `self` | `DetectSceneCutsStatus` | Returns a dict with job status and completion percentage of the active DetectSceneCuts operation |
| `GetCreateSubtitlesFromAudioStatus` | `self` | `CreateSubtitlesFromAudioStatus` | Returns a dict with job status and completion percentage of the active CreateSubtitlesFromAudio operation |

## `ProjectManager`

| 方法 | 签名 | 返回 | 说明 |
| --- | --- | --- | --- |
| `LoadProject` | `self, projectName: str` | `Project | None` | Loads and returns a project. Returns None if project was not found. |
| `CreateProject` | `self, projectName: str, mediaLocationPath: str | None = None` | `Project | None` | Creates and returns a project. Returns None if projectName exists. |
| `DeleteProject` | `self, projectName: str` | `bool` | Delete project in the current folder. Project must not be currently loaded. |
| `SaveProject` | `self` | `bool` | Saves the currently loaded project with its own name. |
| `GetCurrentProject` | `self` | `Project` | Returns the currently loaded Resolve project |
| `CreateFolder` | `self, folderName: str` | `bool` | Creates a folder. Returns False if it already existed. |
| `GetProjectListInCurrentFolder` | `self` | `list[str]` | Returns a list of project names in current folder |
| `GetFolderListInCurrentFolder` | `self` | `list[str]` | Returns a list of folder names in current folder |
| `GotoRootFolder` | `self` | `bool` | Opens root folder in database |
| `GotoParentFolder` | `self` | `bool` | Opens parent folder of current folder in database. Returns False if current folder has no parent. |
| `OpenFolder` | `self, folderName: str` | `bool` | Opens folder |
| `ImportProject` | `self, filePath: str, projectName: str | None = None` | `bool` | Imports a project from the file |
| `ExportProject` | `self, projectName: str, filePath: str, withStillsAndLUTs = True` | `bool` | Exports project to a file. |
| `ArchiveProject` | `self, projectName: str, filePath: str, isArchiveSrcMedia = True, isArchiveRenderCache = True, isArchiveProxyMedia = Fals` | `bool` | Archives project to a file |
| `RestoreProject` | `self, filePath: str, projectName: str | None = None` | `bool` | Restores a project from the file |
| `GetProjectLastModifiedTime` | `self, projectName: str` | `int` | Returns the last modified time of the project as an epoch timestamp |
| `GetProjectAttributesInCurrentFolder` | `self` | `dict[str, ProjectAttributes]` | Returns a dict of project names mapped to their attributes (lastModifiedDate, creationDate, notes, liveCollaborationMode) for all projects in the current folder |
| `CloseProject` | `self, project: Project` | `bool` | Closes the specified project without saving |
| `GetCurrentFolder` | `self` | `str` | Returns the current folder name |
| `DeleteFolder` | `self, folderName: str` | `bool` | Deletes the specified folder |
| `GetCurrentDatabase` | `self` | `DatabaseInfo` | Returns a dictionary (with keys 'DbType', 'DbName' and optional 'IpAddress') corresponding to the current database connection |
| `GetDatabaseList` | `self` | `list[DatabaseInfo]` | Returns a list of dictionary items (with keys 'DbType', 'DbName' and optional 'IpAddress') corresponding to all the databases added to Resolve |
| `SetCurrentDatabase` | `self, dbInfo: DatabaseInfo` | `bool` | Switches current database connection to the database specified by the keys below, and closes any open project |
| `LoadCloudProject` | `self, cloudSettings: CloudSettings` | `Project | None` | Loads and returns a cloud project with the given cloud settings. Returns None if not found |
| `CreateCloudProject` | `self, cloudSettings: CloudSettings` | `Project | None` | Creates and returns a cloud project |
| `ImportCloudProject` | `self, filePath: str, cloudSettings: CloudSettings` | `bool` | Imports a cloud project from the file path with given cloud settings |
| `RestoreCloudProject` | `self, folderPath: str, cloudSettings: CloudSettings` | `bool` | Restores a cloud project from the folder path with given cloud settings |

## `Resolve`

| 方法 | 签名 | 返回 | 说明 |
| --- | --- | --- | --- |
| `GetProjectManager` | `self` | `ProjectManager` | Returns the project manager object for currently open database |
| `GetMediaStorage` | `self` | `MediaStorage` | Returns the media storage object to query and act on media locations |
| `Fusion` | `self` | `Fusion` | Starting point for Fusion scripts |
| `GetCurrentProject` | `self` | `Project` | Returns the currently loaded Resolve project |
| `GetCurrentTimeline` | `self` | `Timeline` | Returns the currently loaded timeline |
| `GetMediaPool` | `self` | `MediaPool` | Returns the MediaPool object for the current project |
| `GetGallery` | `self` | `Gallery` | Returns the Gallery object for the current project |
| `OpenPage` | `self, pageName: str` | `bool` | Switches DaVinci Resolve Page. pageName can be: 'media', 'photo', 'cut', 'edit', 'fusion', 'color', 'fairlight', 'deliver' |
| `GetCurrentPage` | `self` | `str` | Returns current DaVinci Resolve Page: 'media', 'photo', 'cut', 'edit', 'fusion', 'color', 'fairlight', 'deliver' |
| `SetHighPriority` | `self, highPriority: bool` | `bool` | Sets the script execution priority to high or normal |
| `GetVersion` | `self` | `list[int | str]` | Returns list of product version fields in [major, minor, patch, build, suffix] format |
| `GetVersionString` | `self` | `str` | Returns product version in major.minor.patch[suffix].build format |
| `GetProductName` | `self` | `str` | Returns product name |
| `IsStudio` | `self` | `bool` | Returns whether this is the Studio version of the product |
| `GetExtrasPackages` | `self` | `list[ExtrasPackageInfo]` | Returns the Extras Download Manager packages available for this system: optional packages, mostly AI models, that Studio and AI functions require. See README.md |
| `InstallExtrasPackage` | `self, name: str` | `bool` | Queues the installation of an Extras Package, as given by the 'name' of a GetExtrasPackages() entry. Poll GetExtrasPackages() for status and progress. |
| `UninstallExtrasPackage` | `self, name: str` | `bool` | Queues removal of an Extras Package, as given by the 'name' of a GetExtrasPackages() entry. Cancels an ongoing download. |
| `GetLayoutPresetList` | `self` | `list[str]` | Returns a list of available UI layout preset names |
| `GetEffectsList` | `self, mediaType: str | None = None` | `list[EffectInfo]` | Returns all available effects that can be applied to a timeline item. Optional argument mediaType: \"video\" (default), \"photo\" or \"audio\" restricts the lis |
| `LoadLayoutPreset` | `self, presetName: str` | `bool` | Loads UI layout from saved preset |
| `UpdateLayoutPreset` | `self, presetName: str` | `bool` | Overwrites preset named 'presetName' with current UI layout |
| `ExportLayoutPreset` | `self, presetName: str, presetFilePath: str` | `bool` | Exports preset named 'presetName' to path 'presetFilePath' |
| `DeleteLayoutPreset` | `self, presetName: str` | `bool` | Deletes preset named 'presetName' |
| `SaveLayoutPreset` | `self, presetName: str` | `bool` | Saves current UI layout as a preset |
| `ImportLayoutPreset` | `self, presetFilePath: str, presetName: str | None = None` | `bool` | Imports UI layout preset from file |
| `Quit` | `self` | `bool` | Quits the Resolve App |
| `ImportRenderPreset` | `self, presetPath: str` | `bool` | Import a render preset from a file and select it |
| `ExportRenderPreset` | `self, presetName: str, exportPath: str` | `bool` | Export a render preset to a file |
| `GetBurnInPresetList` | `self` | `list[str]` | Returns a list of available data burn in preset names |
| `DeleteBurnInPreset` | `self, presetName: str` | `bool` | Deletes the named data burn in preset |
| `ImportBurnInPreset` | `self, presetPath: str` | `bool` | Import a data burn in preset from a file |
| `ExportBurnInPreset` | `self, presetName: str, exportPath: str` | `bool` | Export a data burn in preset to a file |
| `GetKeyboardPresetList` | `self` | `list[str]` | Returns a list of available keyboard preset names |
| `LoadKeyboardPreset` | `self, presetName: str` | `bool` | Loads the named keyboard preset |
| `DeleteKeyboardPreset` | `self, presetName: str` | `bool` | Deletes the named keyboard preset |
| `GetCurrentKeyboardPreset` | `self` | `str` | Returns the name of the currently active keyboard preset |
| `ImportKeyboardPreset` | `self, filePath: str, presetName: str | None = None` | `bool` | Imports a keyboard preset from file. Uses file base name as preset name if not specified. |
| `ExportKeyboardPreset` | `self, presetName: str, exportPath: str` | `bool` | Exports the named keyboard preset to the specified file path |
| `GetKeyframeMode` | `self` | `KeyframeMode` | Returns the currently set keyframe mode, one of the resolve.KEYFRAME_MODE_* constants. |
| `SetKeyframeMode` | `self, keyframeMode: KeyframeMode` | `bool` | Set keyframe mode |
| `GetFairlightPresets` | `self` | `list[str]` | Returns a list of Fairlight presets by name |
| `DisableBackgroundTasksForCurrentResolveSession` | `self` | `` | Disables all background tasks for current Resolve session |
| `ValidateDCTL` | `self, dctlSource: str` | `str | None` | Validates DCTL source code. Returns None on success, error string on failure. |
| `EncryptDCTL` | `self, inputPath: str, encryptDCTLOptions: EncryptDCTLOptions | None = None` | `bool` | Encrypts the DCTL at inputPath and writes it to an output folder. |
| `GetUserPreferencesPresetList` | `self` | `list[str]` | Returns a list of available user preferences preset names |
| `LoadUserPreferencesPreset` | `self, presetName: str` | `bool` | Loads the named user preferences preset |
| `SaveUserPreferencesPreset` | `self, presetName: str` | `bool` | Saves current user preferences as a preset with the given name |
| `DeleteUserPreferencesPreset` | `self, presetName: str` | `bool` | Deletes the named user preferences preset |
| `ImportUserPreferencesPreset` | `self, filePath: str, presetName: str | None = None` | `bool` | Imports a user preferences preset from file. Uses file base name as preset name if not specified. |
| `ExportUserPreferencesPreset` | `self, presetName: str, exportPath: str` | `bool` | Exports the named user preferences preset to the specified file path |

## `Timeline`

| 方法 | 签名 | 返回 | 说明 |
| --- | --- | --- | --- |
| `GetName` | `self` | `str` | Returns the timeline name. |
| `SetName` | `self, timelineName: str` | `bool` | Sets the timeline name if timelineName (string) is unique. |
| `GetIsEnabled` | `self` | `bool` | Returns True if the timeline is enabled. |
| `SetIsEnabled` | `self, enabled: bool` | `bool` | Enables/disables the timeline and returns True if successful. |
| `GetStartFrame` | `self` | `int` | Returns the frame number at the start of timeline. |
| `GetEndFrame` | `self` | `int` | Returns the frame number at the end of timeline. |
| `GetTrackCount` | `self, trackType: TrackType` | `int` | Returns the number of tracks for the given TrackType. |
| `GetItemListInTrack` | `self, trackType: TrackType, index: int` | `list[TimelineItem]` | Returns a list of timeline items on specified track. |
| `GetSelectedClips` | `self` | `list[TimelineItem]` | Returns the currently selected timeline items |
| `GetCurrentTimecode` | `self` | `str` | Returns a string timecode representation for the current playhead position. |
| `SetCurrentTimecode` | `self, timecode: str` | `bool` | Sets current playhead position from input timecode. |
| `GetCurrentVideoItem` | `self` | `TimelineItem | None` | Returns the current video timeline item. |
| `AddMarker` | `self, frameId: int, color: MarkerColor, name: str, note: str, duration: int, customData: str | None = None` | `bool` | Creates a new marker at given frameId position. |
| `DeleteMarkersByColor` | `self, color: MarkerColor | Literal['All']` | `bool` | Deletes all timeline markers of the specified color. |
| `DeleteMarkerAtFrame` | `self, frameNum: int` | `bool` | Deletes the timeline marker at the given frame number. |
| `DeleteMarkerByCustomData` | `self, customData: str` | `bool` | Delete first matching marker with specified customData. |
| `GetMarkers` | `self` | `dict[int, MarkerInfo]` | Returns a dict (frameId -> {information}) of all markers. |
| `GetMarkerByCustomData` | `self, customData: str` | `MarkerInfo` | Returns marker {information} for the first matching marker with specified customData. |
| `UpdateMarkerCustomData` | `self, frameId: int, customData: str` | `bool` | Updates customData for the marker at given frameId position. |
| `GetMarkerCustomData` | `self, frameId: int` | `str` | Returns customData string for the marker at given frameId position. |
| `GetCurrentClipThumbnailImage` | `self` | `ThumbnailData` | Returns a dict with data containing raw thumbnail image data for current media in the Color Page. |
| `ExportFrame` | `self, frameOffset: int, exportFrameOptions: ExportFrameOptions | None = None` | `ExportFrameResult` | Exports the frame at frameOffset (0-based offset from the timeline start) as a still image per exportFrameOptions. |
| `ExportThumbnails` | `self, frames: list[int | ThumbnailFrame], exportThumbnailsOptions: ExportThumbnailsOptions | None = None` | `ExportThumbnailsResult` | Renders the given frames (0-based offsets from the timeline start) into a single grid image, filled in the order given |
| `AddTrack` | `self, trackType: TrackType, subTrackType: str | None = None` | `bool` | Adds track of TrackType. Optional argument subTrackType. |
| `DeleteTrack` | `self, trackType: TrackType, trackIndex: int` | `bool` | Deletes track of trackType and given trackIndex. 1 <= trackIndex <= GetTrackCount(trackType). |
| `GetTrackSubType` | `self, trackType: TrackType, trackIndex: int` | `str` | Returns an audio track's format. |
| `SetTrackEnable` | `self, trackType: TrackType, trackIndex: int, enabled: bool` | `bool` | Enables/Disables track with given trackType and trackIndex |
| `GetIsTrackEnabled` | `self, trackType: TrackType, trackIndex: int` | `bool` | Returns True if track with given trackType and trackIndex is enabled. |
| `SetTrackLock` | `self, trackType: TrackType, trackIndex: int, locked: bool` | `bool` | Locks/Unlocks track with given trackType and trackIndex |
| `GetIsTrackLocked` | `self, trackType: TrackType, trackIndex: int` | `bool` | Returns True if track with given trackType and trackIndex is locked. |
| `DeleteClips` | `self, timelineItems: list[TimelineItem], rippleDelete = False` | `bool` | Deletes specified TimelineItems from the timeline, performing ripple delete if second argument is True. |
| `DeleteGaps` | `self` | `bool` | Deletes all gaps between clips on the timeline, rippling content to close the gaps. |
| `SetClipsLinked` | `self, timelineItems: list[TimelineItem], linked: bool` | `bool` | Links or unlinks the specified TimelineItems depending on second argument. |
| `MoveItems` | `self, timelineItems: list[TimelineItem], position: TimelineItemPosition, moveLinkedItems = True, subframePrecision = Fal` | `bool` | Moves the leftmost TimelineItem (lowest track on ties) to the given position and the other items relative to it. Fails if any item cannot reach its destination. |
| `NormalizeAudioLevel` | `self, timelineItems: list[TimelineItem], normalizeAudioOptions: NormalizeAudioOptions | None = None` | `bool` | Normalizes the audio level of specified TimelineItems using the given normalizeAudioOptions. |
| `AutoAlignClips` | `self, timelineItems: list[TimelineItem], autoAlignOptions: AutoAlignOptions | None = None` | `bool` | Aligns specified TimelineItems using the given options. Returns True if successful, False otherwise. |
| `GetNormalizeAudioModes` | `self` | `list[str]` | Returns the list of valid normalizationMode strings for NormalizeAudioLevel. |
| `GetTrackName` | `self, trackType: TrackType, trackIndex: int` | `str` | Returns the track name for track indicated by trackType and index. |
| `SetTrackName` | `self, trackType: TrackType, trackIndex: int, name: str` | `bool` | Sets the track name for track indicated by trackType and index. |
| `DuplicateTimeline` | `self, timelineName: str` | `Timeline` | Duplicates the timeline and returns the created timeline. |
| `GrabStill` | `self` | `GalleryStill` | Grabs still from the current video clip. Returns a GalleryStill object. |
| `GrabAllStills` | `self, stillFrameSource: int` | `list[GalleryStill]` | Grabs stills from all clips at 'stillFrameSource' (1=First frame, 2=Middle frame). |
| `CreateCompoundClip` | `self, timelineItems: list[TimelineItem], clipInfo: CompoundClipOptions | None = None` | `TimelineItem` | Creates a compound clip of input timeline items. |
| `CreateFusionClip` | `self, timelineItems: list[TimelineItem]` | `TimelineItem` | Creates a Fusion clip of input timeline items. |
| `Export` | `self, fileName: str, exportType: TimelineExportType, exportSubtype: TimelineExportSubtype` | `bool` | Exports timeline to 'fileName' as per input exportType & exportSubtype format. See README.md section 'Looking up timeline export properties'. |
| `GetSettings` | `self` | `TimelineSettings | ProjectSettings` | Returns a dict with all timeline settings, or the project settings when useCustomSettings is '0'. See README.md section 'Looking up Project and Clip properties' |
| `SetSettings` | `self, settings: TimelineSettings` | `bool` | Sets the timeline settings with specified dict of setting names and values. See README.md section 'Looking up Project and Clip properties'. |
| `GetStartTimecode` | `self` | `str` | Returns the start timecode for the timeline. |
| `SetStartTimecode` | `self, timecode: str` | `bool` | Set the start timecode of the timeline to the string 'timecode'. |
| `ImportIntoTimeline` | `self, filePath: str, importOptions: AAFImportOptions | None = None` | `bool` | Imports timeline items from an AAF file. |
| `InsertGeneratorIntoTimeline` | `self, generatorName: str` | `TimelineItem` | Inserts a generator into the timeline. |
| `InsertFusionGeneratorIntoTimeline` | `self, generatorName: str` | `TimelineItem` | Inserts a Fusion generator into the timeline. |
| `InsertFusionCompositionIntoTimeline` | `self` | `TimelineItem` | Inserts a Fusion composition into the timeline. |
| `InsertOFXGeneratorIntoTimeline` | `self, generatorName: str` | `TimelineItem` | Inserts an OFX generator into the timeline. |
| `InsertTitleIntoTimeline` | `self, titleName: str` | `TimelineItem` | Inserts a title into the timeline. |
| `InsertFusionTitleIntoTimeline` | `self, titleName: str` | `TimelineItem` | Inserts a Fusion title into the timeline. |
| `CreateSubtitlesFromAudio` | `self, autoCaptionSettings: AutoCaptionSettings | None = None` | `bool` | Creates subtitles from audio for the timeline. |
| `GetUniqueId` | `self` | `str` | Returns a unique ID for the timeline |
| `DetectSceneCuts` | `self` | `bool` | Detects and makes scene cuts along the timeline. |
| `ConvertTimelineToStereo` | `self` | `bool` | Converts timeline to stereo. |
| `GetNodeGraph` | `self` | `Graph` | Returns the timeline's node graph object. |
| `AnalyzeDolbyVision` | `self, timelineItems: list[TimelineItem], analysisType: DolbyVisionAnalysisType` | `bool` | Analyzes Dolby Vision on clips present on the timeline. |
| `GetMediaPoolItem` | `self` | `MediaPoolItem | None` | Returns the media pool item corresponding to the timeline |
| `GetMarkInOut` | `self` | `MarkInOut` | Returns dict of in/out marks set. |
| `SetMarkInOut` | `self, markIn: int, markOut: int, markType: MarkType | None = None` | `bool` | Sets mark in/out of type MarkType (default: 'all') |
| `ClearMarkInOut` | `self, markType: MarkType | None = None` | `bool` | Clears mark in/out of type MarkType (default: 'all') |
| `GetVoiceIsolationState` | `self, trackIndex: int` | `VoiceIsolationState` | Returns the Voice Isolation State as a dict. |
| `SetVoiceIsolationState` | `self, trackIndex: int, voiceIsolationState: VoiceIsolationState` | `bool` | Sets Voice Isolation state of audio track. |
| `SetOutputBlanking` | `self, outputBlanking: OutputBlanking` | `bool` | Sets the output blanking for the timeline. Accepts a dictionary with keys 'Top', 'Bottom', 'Left' and 'Right'. The values are in pixels. |
| `GetOutputBlanking` | `self` | `OutputBlanking` | Returns the output blanking for the timeline as a dictionary with keys 'Top', 'Bottom', 'Left' and 'Right'. The values are in pixels. |

## `TimelineItem`

| 方法 | 签名 | 返回 | 说明 |
| --- | --- | --- | --- |
| `GetType` | `self` | `str` | Returns the type of the item: 'video', 'audio', 'generator' or 'transition' |
| `AddTransition` | `self, transitionOptions: TransitionOptions` | `TimelineItem | None` | Adds a transition of the given type/category to the start or end of this item. Returns the created transition item or None on failure. |
| `GetName` | `self` | `str` | Returns the item name |
| `SetName` | `self, name: str` | `bool` | Sets the clip's name to name. |
| `GetStart` | `self, subframePrecision = False` | `float` | Returns the start frame position on the timeline. Returns fractional frames if subframe_precision is True |
| `GetEnd` | `self, subframePrecision = False` | `float` | Returns the end frame position on the timeline. Returns fractional frames if subframe_precision is True |
| `GetSourceStartFrame` | `self` | `int` | Returns the start frame position of the media pool clip in the timeline clip |
| `GetSourceEndFrame` | `self` | `int` | Returns the end frame position of the media pool clip in the timeline clip |
| `GetSourceStartTime` | `self` | `float` | Returns the start time position of the media pool clip in the timeline clip |
| `GetSourceEndTime` | `self` | `float` | Returns the end time position of the media pool clip in the timeline clip |
| `GetDuration` | `self, subframePrecision = False` | `float` | Returns the item duration. Returns fractional frames if subframe_precision is True |
| `GetLeftOffset` | `self, subframePrecision = False` | `float` | Returns the maximum extension by frame for clip from left side. Returns fractional frames if subframe_precision is True |
| `GetRightOffset` | `self, subframePrecision = False` | `float` | Returns the maximum extension by frame for clip from right side. Returns fractional frames if subframe_precision is True |
| `SetLeftOffset` | `self, offset: float, subframePrecision = False, updateLinkedItems = True` | `bool` | Sets the clip's left (start) edit point to have the given offset (in frames) available. If subframePrecision is True, fractional offsets are allowed for audio c |
| `SetRightOffset` | `self, offset: float, subframePrecision = False, updateLinkedItems = True` | `bool` | Sets the clip's right (end) edit point to have the given offset (in frames) available. If subframePrecision is True, fractional offsets are allowed for audio cl |
| `GetFusionCompCount` | `self` | `int` | Returns number of Fusion compositions associated with the timeline item |
| `GetFusionCompNameList` | `self` | `list[str]` | Returns a list of Fusion composition names associated with the timeline item |
| `GetFusionCompByIndex` | `self, compIndex: int` | `FusionComp | None` | Returns the Fusion composition object based on given index. 1 <= compIndex <= timelineItem.GetFusionCompCount() |
| `GetFusionCompByName` | `self, compName: str` | `FusionComp | None` | Returns the Fusion composition object based on given name |
| `AddFusionComp` | `self` | `FusionComp` | Adds a new Fusion composition associated with the timeline item |
| `AddEffect` | `self, category: str, id: str` | `Effect | None` | Applies the effect with the provided category ('fusion', 'ofx' or 'audio') and id (see Resolve.GetEffectsList) to this timeline item |
| `GetEffects` | `self, category: str` | `list[Effect]` | Returns the effects of the given category ('fusion', 'ofx' or 'audio') applied to this timeline item |
| `DeleteEffects` | `self, effects: list[Effect]` | `bool` | Removes the given effects from this timeline item |
| `GetMediaPoolItem` | `self` | `MediaPoolItem | None` | Returns the media pool item corresponding to the timeline item if one exists |
| `AddMarker` | `self, frameId: int, color: MarkerColor, name: str, note: str, duration: int, customData: str | None = None` | `bool` | Creates a new marker at given frameId position and with given marker information. 'customData' is optional and helps to attach user specific data to the marker |
| `DeleteMarkersByColor` | `self, color: MarkerColor | Literal['All']` | `bool` | Deletes all markers of the specified color from the timeline item. 'All' as argument deletes all color markers |
| `DeleteMarkerAtFrame` | `self, frameNum: int` | `bool` | Deletes marker at frame number from the timeline item |
| `DeleteMarkerByCustomData` | `self, customData: str` | `bool` | Deletes first matching marker with specified customData |
| `ExportFrame` | `self, frameOffset: int, exportFrameOptions: ExportFrameOptions | None = None` | `ExportFrameResult` | Exports the frame at frameOffset (0-based offset from the item start) as a still image per exportFrameOptions. |
| `ExportThumbnails` | `self, frames: list[int | ThumbnailFrame], exportThumbnailsOptions: ExportThumbnailsOptions | None = None` | `ExportThumbnailsResult` | Renders the given frames (0-based offsets from the item start) into a single grid image, filled in the order given |
| `GetMarkers` | `self` | `dict[int, MarkerInfo]` | Returns a dict (frameId -> {information}) of all markers and dicts with their information |
| `GetMarkerByCustomData` | `self, customData: str` | `MarkerInfo` | Returns marker {information} for the first matching marker with specified customData |
| `UpdateMarkerCustomData` | `self, frameId: int, customData: str` | `bool` | Updates customData (string) for the marker at given frameId position. CustomData is not exposed via UI and is useful for scripting developer to attach any user  |
| `GetMarkerCustomData` | `self, frameId: int` | `str` | Returns customData string for the marker at given frameId position |
| `SetProperties` | `self, properties: TimelineItemProperties` | `bool` | Sets the item properties with specified dict of property keys and values. See README.md section 'Looking up Timeline item properties'. |
| `GetProperties` | `self` | `TimelineItemProperties` | Returns a dict with all supported item properties. See README.md section 'Looking up Timeline item properties'. |
| `SetSpeed` | `self, speedOptions: SpeedOptions` | `bool` | Sets the Clip Speed |
| `GetSpeed` | `self` | `SpeedOptions` | Returns the clip speed options |
| `AddFlag` | `self, color: FlagColor` | `bool` | Adds a flag with given color (string) |
| `GetFlagList` | `self` | `list[str]` | Returns a list of flag colors assigned to the item |
| `ClearFlags` | `self, color: FlagColor | Literal['All']` | `bool` | Clears flags of the specified color. An 'All' argument is supported to clear all flags |
| `GetStereoConvergenceValues` | `self` | `dict[int, float]` | Returns a dict (offset -> value) of keyframe offsets and respective convergence values |
| `GetStereoLeftFloatingWindowParams` | `self` | `dict[int, FloatingWindowParams]` | For the LEFT eye -> returns a dict (offset -> dict) of keyframe offsets and respective floating window params |
| `GetStereoRightFloatingWindowParams` | `self` | `dict[int, FloatingWindowParams]` | For the RIGHT eye -> returns a dict (offset -> dict) of keyframe offsets and respective floating window params |
| `GetClipColor` | `self` | `ClipColor | Literal['']` | Returns the item color as a string |
| `SetClipColor` | `self, colorName: ClipColor` | `bool` | Sets the item color based on the colorName (string) |
| `ClearClipColor` | `self` | `bool` | Clears the item color |
| `ImportFusionComp` | `self, path: str` | `FusionComp` | Imports a Fusion composition from given file path by creating and adding a new composition for the item |
| `ExportFusionComp` | `self, path: str, compIndex: int` | `bool` | Exports the Fusion composition based on given index to the path provided |
| `DeleteFusionCompByName` | `self, compName: str` | `bool` | Deletes the named Fusion composition |
| `LoadFusionCompByName` | `self, compName: str` | `FusionComp` | Loads the named Fusion composition as the active composition |
| `RenameFusionCompByName` | `self, oldName: str, newName: str` | `bool` | Renames the Fusion composition identified by oldName |
| `RenameVersionByName` | `self, oldName: str, newName: str, versionType: int` | `bool` | Renames the color version identified by oldName and versionType (0 - local, 1 - remote) |
| `DeleteVersionByName` | `self, versionName: str, versionType: int` | `bool` | Deletes a color version by name and versionType (0 - local, 1 - remote) |
| `LoadVersionByName` | `self, versionName: str, versionType: int` | `bool` | Loads a named color version as the active version. versionType: 0 - local, 1 - remote |
| `AddVersion` | `self, versionName: str, versionType: int` | `bool` | Adds a new color version for a video clip based on versionType (0 - local, 1 - remote) |
| `GetVersionNameList` | `self, versionType: int` | `list[str]` | Returns a list of all color versions for the given versionType (0 - local, 1 - remote) |
| `SetCDL` | `self, CDL: CDL` | `bool` | Sets CDL values on the node. Keys of map are: 'NodeIndex', 'Slope', 'Offset', 'Power', 'Saturation' |
| `GetCDL` | `self, nodeIndex: int` | `CDL` | Returns the ASC CDL equivalent of the primaries of the node at nodeIndex, as the dict |
| `AddTake` | `self, mediaPoolItem: MediaPoolItem, startFrame: int | None = None, endFrame: int | None = None` | `bool` | Adds mediaPoolItem as a new take. Initializes a take selector for the timeline item if needed. By default, the full clip extents is added. startFrame and endFra |
| `GetSelectedTakeIndex` | `self` | `int` | Returns the index of the currently selected take, or 0 if the clip is not a take selector |
| `GetTakesCount` | `self` | `int` | Returns the number of takes in take selector, or 0 if the clip is not a take selector |
| `AnalyzeAudioLevels` | `self, standard: str` | `AudioLevelsInfo` | Analyzes audio loudness levels for this timeline item. 'standard' is a mode name from timeline.GetNormalizeAudioModes(), excluding the peak-only 'Sample Peak Pr |
| `GetTakeByIndex` | `self, idx: int` | `TakeInfo | None` | Returns a dict with take info for specified index |
| `DeleteTakeByIndex` | `self, idx: int` | `bool` | Deletes a take by index, 1 <= idx <= number of takes |
| `SelectTakeByIndex` | `self, idx: int` | `bool` | Selects a take by index, 1 <= idx <= number of takes |
| `FinalizeTake` | `self` | `bool` | Finalizes take selection |
| `CopyGrades` | `self, tgtTimelineItems: list[TimelineItem]` | `bool` | Copies the current node stack layer grade to the same layer for each item in tgtTimelineItems. |
| `ApplyAutoColor` | `self` | `bool` | Analyses the clip and applies the automatic balance and grade to frame the playhead is on, or from the first frame of the clip when it is not the current one. R |
| `SetAutoColorEnabled` | `self, enabled: bool` | `bool` | Enables or disables the grade a previous ApplyAutoColor() applied |
| `GetAutoColorEnabled` | `self` | `bool | None` | Returns whether auto color is applied and enabled, none if it has no auto color |
| `ClearAutoColor` | `self` | `bool` | Discards auto-color grades |
| `CopyAttributes` | `self, targetItems: list[TimelineItem], options: CopyAttributesOptions` | `bool` | Pastes the selected attributes from this item onto each item in targetItems. Equivalent to the Edit page's \"Paste Attributes\". |
| `GetClipEnabled` | `self` | `bool` | Gets clip enabled status |
| `SetClipEnabled` | `self, enabled: bool` | `bool` | Sets clip enabled based on argument |
| `GetCurrentVersion` | `self` | `VersionInfo` | Returns the current version of the video clip. The returned value will have the keys versionName and versionType (0 - local, 1 - remote) |
| `UpdateSidecar` | `self` | `bool` | Updates sidecar file for BRAW clips or RMD file for R3D clips |
| `GetUniqueId` | `self` | `str` | Returns a unique ID for the timeline item |
| `LoadBurnInPreset` | `self, presetName: str` | `bool` | Loads user defined data burn in preset for clip when supplied presetName (string). |
| `CreateMagicMask` | `self, mode: str` | `bool` | Creates a magic mask. mode can be 'F' (forward), 'B' (backward), or 'BI' (bidirectional) |
| `RegenerateMagicMask` | `self` | `bool` | Regenerates the magic mask |
| `Stabilize` | `self` | `bool` | Performs stabilization on the clip |
| `SmartReframe` | `self` | `bool` | Performs Smart Reframe, tracking the subject and repositioning it within the item's existing frame. It does not itself crop or rescale, so the frame must alread |
| `GetNodeGraph` | `self, layerIdx: int | None = None` | `Graph` | Returns the clip's node graph object at layerIdx (int, optional). Returns the first layer if layerIdx is skipped. 1 <= layerIdx <= project.GetSetting('nodeStack |
| `GetColorGroup` | `self` | `ColorGroup | None` | Returns the clip's color group if one exists |
| `AssignToColorGroup` | `self, colorGroup: ColorGroup` | `bool` | Assigns the clip to the given ColorGroup. ColorGroup must be an existing group in the current project |
| `RemoveFromColorGroup` | `self` | `bool` | Removes the clip from its ColorGroup |
| `ExportLUT` | `self, exportType: ExportLutType, path: str` | `bool` | Exports a LUT of the size given by 'exportType', saving it in the provided 'path' |
| `GetLinkedItems` | `self` | `list[TimelineItem]` | Returns a list of linked timeline items |
| `GetTrackTypeAndIndex` | `self` | `list[str | int]` | Returns a list of two values that correspond to the TimelineItem's trackType (string) and trackIndex (int) respectively |
| `GetPosition` | `self, subframePrecision = False` | `TimelineItemPosition` | Returns the TimelineItem's current absolute position. Returns a fractional frame if subframePrecision is True |
| `SetPosition` | `self, position: TimelineItemPosition, moveLinkedItems = True, subframePrecision = False` | `bool` | Updates the TimelineItem's position on the timeline. If subframePrecision is True, fractional startFrame values are allowed for audio clips when the 'Align audi |
| `GetSourceAudioChannelMapping` | `self` | `str` | Returns a string with TimelineItem's audio mapping information |
| `SetSourceAudioChannelMapping` | `self, audioMapping: str` | `bool` | Sets source audio channel mapping from a JSON string. |
| `GetIsColorOutputCacheEnabled` | `self` | `bool` | Returns if the cache corresponding to cache_type is enabled |
| `GetIsFusionOutputCacheEnabled` | `self` | `str` | Returns if the cache corresponding to cache_type is enabled (or auto) |
| `SetColorOutputCache` | `self, enabled: bool` | `bool` | Sets caching to enabled or disabled. Equivalent to clip context menu action 'Render Cache Color Output' |
| `SetFusionOutputCache` | `self, cacheValue: str` | `bool` | Sets caching to auto, enabled or disabled. Equivalent to clip context menu action 'Render Cache Fusion Output' |
| `GetVoiceIsolationState` | `self` | `VoiceIsolationState` | Returns the Voice Isolation State as a dict {isEnabled, amount}, of the timelineItem |
| `SetVoiceIsolationState` | `self, state: VoiceIsolationState` | `bool` | Sets Voice Isolation state of the timelineItem to the given VoiceIsolationState of {isEnabled (bool), amount (int)}. amount is in range of [0, 100]. |
| `ResetAllNodeColors` | `self` | `bool` | Resets node color for all nodes in the active version of the clip. |
| `SetOutputBlanking` | `self, outputBlanking: OutputBlanking` | `bool` | Sets the output blanking for the clip. Accepts a dictionary with keys 'Top', 'Bottom', 'Left' and 'Right'. The values are in pixels. |
| `GetOutputBlanking` | `self` | `OutputBlanking` | Returns the output blanking for the clip as a dictionary with keys 'Top', 'Bottom', 'Left' and 'Right'. The values are in pixels. The dictionary will be empty i |
| `SetUseTimelineForOutputBlanking` | `self, useTimelineOutputBlanking: bool` | `bool` | Sets the flag to use the timeline's output blanking for the clip. |
| `GetUseTimelineForOutputBlanking` | `self` | `bool` | Gets the flag to use the timeline's output blanking for the clip. |
| `PerformMulticamSmartSwitch` | `self, smartSwitchSettings: SmartSwitchSettings` | `bool` | Performs Multicam SmartSwitch on the multicam TimelineItem using the given smartSwitchSettings |
| `FlattenMulticam` | `self, gradeOption: FlattenMulticamGrade` | `bool` | Flattens the multicam TimelineItem, using the grade source specified by gradeOption |
| `GetFades` | `self` | `FadeInfo` | Returns a dict {FadeIn, FadeOut} of the fade durations (in frames) for the item's video or audio fader |
| `SetFades` | `self, fades: FadeInfo` | `bool` | Sets the fade durations (in frames) for the item's video or audio fader from a dict {FadeIn, FadeOut} |
| `RippleDeleteSilence` | `self, removeSilenceOptions: RemoveSilenceOptions | None = None` | `bool` | Ripple deletes silent portions from this audio TimelineItem. |
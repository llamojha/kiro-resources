---
name: "remotion"
displayName: "Remotion Video Creation"
description: "Create programmatic videos with React using Remotion's powerful animation and rendering engine"
keywords: ["video", "animation", "react", "remotion", "programmatic video", "motion graphics", "video editing", "typescript"]
---

# Onboarding

## Step 1: Validate Remotion setup
Before using Remotion, ensure the following are installed:
- **Node.js 18+**: Remotion requires modern Node.js
  - Verify with: `node --version`
- **Remotion CLI**: Install globally or use npx
  - Verify with: `npx remotion --version`
- **FFmpeg**: Required for video rendering
  - Verify with: `ffmpeg -version`

## Step 2: Initialize Remotion project (if needed)
If starting a new project:
```bash
npx create-remotion@latest
```

## Step 3: Add development hooks
Add a hook to `.kiro/hooks/remotion-preview.kiro.hook`:

```json
{
  "enabled": true,
  "name": "Start Remotion Studio",
  "description": "Launch Remotion Studio for video preview and development",
  "version": "1",
  "when": {
    "type": "userTriggered"
  },
  "then": {
    "type": "executeCommand",
    "command": "npx remotion studio"
  }
}
```

# When to Load Steering Files
- Creating video compositions → `video-compositions.md`
- Working with animations and timing → `animations-timing.md`
- Managing assets (images, audio, fonts) → `asset-management.md`
- Audio and sound integration → `audio-integration.md`
- Rendering and export workflows → `rendering-export.md`
- Performance optimization → `performance-optimization.md`

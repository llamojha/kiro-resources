# Rendering and Export

## Basic Rendering
Render your composition to video:

```bash
# Render specific composition
npx remotion render MyVideo out/video.mp4

# Render with custom props
npx remotion render MyVideo out/video.mp4 --props='{"title":"Custom Title"}'

# Render specific frame range
npx remotion render MyVideo out/video.mp4 --frames=0-150
```

## Render Configuration
Customize output settings:

```bash
# High quality render
npx remotion render MyVideo out/video.mp4 \
  --codec=h264 \
  --crf=18 \
  --pixel-format=yuv420p

# Fast preview render
npx remotion render MyVideo out/preview.mp4 \
  --codec=h264 \
  --crf=28 \
  --scale=0.5

# Transparent video (ProRes 4444)
npx remotion render MyVideo out/transparent.mov \
  --codec=prores \
  --prores-profile=4444
```

## Programmatic Rendering
Render from Node.js:

```tsx
import { bundle } from '@remotion/bundler';
import { renderMedia, selectComposition } from '@remotion/renderer';

const bundleLocation = await bundle({
  entryPoint: './src/index.ts',
});

const composition = await selectComposition({
  serveUrl: bundleLocation,
  id: 'MyVideo',
});

await renderMedia({
  composition,
  serveUrl: bundleLocation,
  codec: 'h264',
  outputLocation: 'out/video.mp4',
  inputProps: {
    title: 'Programmatic Render'
  },
});
```

## Still Image Export
Export single frames:

```bash
# Export specific frame
npx remotion still MyVideo out/frame.png --frame=150

# Export multiple frames
npx remotion still MyVideo out/frames --frames=0,30,60,90
```

## Batch Rendering
Render multiple variations:

```tsx
const variations = [
  { title: 'Video 1', color: 'red' },
  { title: 'Video 2', color: 'blue' },
  { title: 'Video 3', color: 'green' },
];

for (const props of variations) {
  await renderMedia({
    composition,
    serveUrl: bundleLocation,
    codec: 'h264',
    outputLocation: `out/${props.title.replace(' ', '-')}.mp4`,
    inputProps: props,
  });
}
```

## Best Practices
- Use CRF 18-23 for high quality, 28+ for previews
- Choose codec based on use case (H.264 for web, ProRes for editing)
- Render at full resolution, scale down later if needed
- Use frame ranges for testing specific sections
- Batch render variations programmatically
- Monitor render progress and handle errors gracefully

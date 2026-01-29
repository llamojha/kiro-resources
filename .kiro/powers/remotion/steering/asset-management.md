# Asset Management

## Static Assets
Import assets using staticFile():

```tsx
import { Img, staticFile } from 'remotion';

export const ImageComponent = () => {
  return (
    <Img 
      src={staticFile('logo.png')} 
      style={{ width: 200, height: 200 }}
    />
  );
};
```

## Video Assets
Embed videos with proper controls:

```tsx
import { Video, staticFile } from 'remotion';

export const VideoComponent = () => {
  return (
    <Video
      src={staticFile('background-video.mp4')}
      startFrom={30} // Start from frame 30
      endAt={180}    // End at frame 180
      volume={0.5}
    />
  );
};
```

## Font Loading
Load custom fonts:

```tsx
import { loadFont } from '@remotion/google-fonts/Inter';
import { continueRender, delayRender } from 'remotion';

const { fontFamily } = loadFont();

export const TextComponent = () => {
  const [fontsLoaded, setFontsLoaded] = useState(false);
  
  useEffect(() => {
    const handle = delayRender();
    
    loadFont().then(() => {
      setFontsLoaded(true);
      continueRender(handle);
    });
  }, []);
  
  if (!fontsLoaded) return null;
  
  return (
    <div style={{ fontFamily }}>
      Custom font text
    </div>
  );
};
```

## Asset Organization
Structure your assets:

```
public/
├── images/
│   ├── logo.png
│   └── background.jpg
├── videos/
│   └── intro.mp4
├── audio/
│   └── music.mp3
└── fonts/
    └── custom-font.woff2
```

## Best Practices
- Use staticFile() for all asset imports
- Optimize images (WebP for photos, PNG for graphics)
- Compress videos before importing
- Preload fonts to avoid render delays
- Use consistent naming conventions
- Keep assets organized in logical folders

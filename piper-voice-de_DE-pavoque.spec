Name:		piper-voice-de_DE-pavoque
Version:	2023.09.23
Release:	1
Summary:	German female voice for the Piper TTS system
URL:		https://huggingface.co/rhasspy/piper-voices/tree/main/de/de_DE/pavoque/low
License:	MIT
BuildArch:	noarch
Group:		System/Multimedia
Provides:	piper-voice
Provides:	piper-voice-de
Provides:	piper-voice-de_DE

%sourcelist
https://huggingface.co/rhasspy/piper-voices/resolve/main/de/de_DE/pavoque/low/de_DE-pavoque-low.onnx
https://huggingface.co/rhasspy/piper-voices/resolve/main/de/de_DE/pavoque/low/de_DE-pavoque-low.onnx.json

%description
%{summary}

%install
mkdir -p %{buildroot}%{_datadir}/piper/voices
install -c -m 644 %{S:0} %{S:1} %{buildroot}%{_datadir}/piper/voices/

%files
%{_datadir}/piper/voices/*

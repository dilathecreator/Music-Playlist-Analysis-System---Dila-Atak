def get_total_duration(songs):
    # Toplam süre tanımlandı
    total = 0
    for song in songs:
        total += song["sure"]
    return total


def get_most_played_song(songs):
    # En çok dinlenen şarkı tanımlandı
    if not songs:
        return None

    most_played = songs[0]
    for song in songs:
        if song["dinlenme_sayisi"] > most_played["dinlenme_sayisi"]:
            most_played = song
    return most_played


def get_average_duration(songs):
    # Ortalama süre tanımlandı
    if not songs:
        return 0
    total = get_total_duration(songs)
    return total / len(songs)


def print_playlist(songs):
    # Playlist içindeki şarkılar for döngüsüne sokuldu
    print("\n--- ULTRAVIOLENCE ALBUM ANALYSIS ---")
    for song in songs:
        print(
            f"Şarkı: {song['sarki_adi']} | Sanatçı: {song['sanatci_adi']} | Süre: {song['sure']} dk | Dinlenme: {song['dinlenme_sayisi']}")
    print("-" * 35)


def main():
    # Playlist içindeki şarkılar tanımlandı
    playlist = [
        {"sarki_adi": "Cruel World", "sanatci_adi": "Lana Del Rey", "sure": 6.39, "dinlenme_sayisi": 120000000},
        {"sarki_adi": "Ultraviolence", "sanatci_adi": "Lana Del Rey", "sure": 4.11, "dinlenme_sayisi": 250000000},
        {"sarki_adi": "Shades of Cool", "sanatci_adi": "Lana Del Rey", "sure": 5.42, "dinlenme_sayisi": 180000000},
        {"sarki_adi": "Brooklyn Baby", "sanatci_adi": "Lana Del Rey", "sure": 5.51, "dinlenme_sayisi": 320000000},
        {"sarki_adi": "West Coast", "sanatci_adi": "Lana Del Rey", "sure": 4.16, "dinlenme_sayisi": 450000000}
    ]

    # Şarkıları listelenen playlist ekrana yazdırıldı
    print_playlist(playlist)

    # Şarkıların toplam süresi hesaplandı
    total_time = get_total_duration(playlist)
    print(f"\nAlbüm Toplam Süresi: {total_time:.2f} dakika")

    # Şarkıların ortalama süresi hesaplatıldı
    avg_time = get_average_duration(playlist)
    print(f"Ortalama Şarkı Süresi: {avg_time:.2f} dakika")

    # En çok tıklanan şarkı ekrana yazdırıldı
    top_song = get_most_played_song(playlist)
    if top_song:
        print(f"En Çok Dinlenen Şarkı: {top_song['sarki_adi']} ({top_song['dinlenme_sayisi']} dinlenme)")


if __name__ == "__main__":
    main()

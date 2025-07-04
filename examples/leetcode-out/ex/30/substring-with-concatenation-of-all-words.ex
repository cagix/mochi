# Generated by Mochi Elixir compiler
defmodule Main do
  def findSubstring(s, words) do
    try do
      if length(words) == 0 do
        throw({:return, []})
      end

      wordLen = length(Enum.at(words, 0))
      wordCount = length(words)
      totalLen = wordLen * wordCount

      if length(s) < totalLen do
        throw({:return, []})
      end

      freq = %{}
      _ = freq

      {freq} =
        Enum.reduce(_iter(words), {freq}, fn w, {freq} ->
          if if is_map(freq), do: Map.has_key?(freq, w), else: Enum.member?(freq, w) do
            freq = Map.put(freq, w, Enum.at(freq, w) + 1)
          else
            freq = Map.put(freq, w, 1)
          end

          {freq}
        end)

      _ = freq
      result = []
      _ = result

      {result} =
        Enum.reduce(0..(wordLen - 1), {result}, fn offset, {result} ->
          left = offset
          _ = left
          count = 0
          _ = count
          seen = %{}
          _ = seen
          j = offset
          _ = j

          t1 = fn t1, count, j, left, result, seen ->
            try do
              if j + wordLen <= length(s) do
                word = Enum.slice(s, j, j + wordLen - j)
                j = j + wordLen

                if if is_map(freq), do: Map.has_key?(freq, word), else: Enum.member?(freq, word) do
                  if if is_map(seen), do: Map.has_key?(seen, word), else: Enum.member?(seen, word) do
                    seen = Map.put(seen, word, Enum.at(seen, word) + 1)
                  else
                    seen = Map.put(seen, word, 1)
                  end

                  count = count + 1

                  t2 = fn t2, count, left, seen ->
                    try do
                      if Enum.at(seen, word) > Enum.at(freq, word) do
                        lw = Enum.slice(s, left, left + wordLen - left)
                        seen = Map.put(seen, lw, Enum.at(seen, lw) - 1)
                        left = left + wordLen
                        count = count - 1
                        t2.(t2, count, left, seen)
                      else
                        {:ok, count, left, seen}
                      end
                    catch
                      :break ->
                        {:ok, count, left, seen}
                    end
                  end

                  {_, count, left, seen} = t2.(t2, count, left, seen)
                  _ = count
                  _ = left
                  _ = seen

                  if count == wordCount do
                    result = result ++ [left]
                    lw = Enum.slice(s, left, left + wordLen - left)
                    seen = Map.put(seen, lw, Enum.at(seen, lw) - 1)
                    left = left + wordLen
                    count = count - 1
                  end
                else
                  seen = %{}
                  count = 0
                  left = j
                end

                t1.(t1, count, j, left, result, seen)
              else
                {:ok, count, j, left, result, seen}
              end
            catch
              :break ->
                {:ok, count, j, left, result, seen}
            end
          end

          {_, count, j, left, result, seen} = t1.(t1, count, j, left, result, seen)
          _ = count
          _ = j
          _ = left
          _ = result
          _ = seen
          {result}
        end)

      _ = result
      throw({:return, result})
    catch
      {:return, v} -> v
    end
  end

  def main do
  end

  defp _iter(v) do
    if is_map(v) do
      Map.keys(v)
    else
      v
    end
  end
end

Main.main()
